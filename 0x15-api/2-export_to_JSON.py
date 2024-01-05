#!/usr/bin/python3
'''A Python script to export data in the JSON format'''

import re
import requests
import sys
import json

"""The API's URL"""
API_URL = 'https://jsonplaceholder.typicode.com'

def export_to_json(user_id, user_name, todos):
    """
    Export user's tasks to a JSON file.

    Args:
    - user_id (int): The ID of the user.
    - user_name (str): The username of the user.
    - todos (list): List of tasks associated with the user.

    Returns:
    - None
    """
    filename = f"{user_id}.json"

    tasks_data = {str(user_id): []}

    for todo in todos:
        task_info = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user_name
        }
        tasks_data[str(user_id)].append(task_info)

    with open(filename, 'w') as json_file:
        json.dump(tasks_data, json_file, indent=4)

    print(f"Data exported to {filename}")

if __name__ == '__main__':
    """Check if command line arguments were provided"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    """Check if the argument is a valid user ID"""
    if re.fullmatch(r'\d+', sys.argv[1]):
        user_id = int(sys.argv[1])

        """Get the user's information from the API"""
        user_res = requests.get(f'{API_URL}/users/{user_id}')

        if user_res.status_code == 200:
            user_data = user_res.json()
            user_name = user_data.get('username')

            """Fetch user's TODO list"""
            todos_res = requests.get(f'{API_URL}/todos?userId={user_id}')

            if todos_res.status_code == 200:
                todos_data = todos_res.json()

                """Write the data to a JSON file"""
                export_to_json(user_id, user_name, todos_data)
            else:
                print(f"Failed to fetch TODO list. Status code: {todos_res.status_code}")
        else:
            print(f"Failed to fetch user information. Status code: {user_res.status_code}")
    else:
        print('Invalid user ID format.')
