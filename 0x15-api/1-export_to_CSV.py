#!/usr/bin/python3
'''
A Python script to export data in the CSV format.
'''

import csv
import requests
import sys

# The API's URL
API_URL = 'https://jsonplaceholder.typicode.com'

def write_to_csv(user_id, user_name, todos):
    """
    Write user's tasks to a CSV file.

    Args:
    - user_id (int): The ID of the user.
    - user_name (str): The username of the user.
    - todos (list): List of tasks associated with the user.

    Returns:
    - None
    """
    filename = f"{user_id}.csv"
    
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": str(todo.get('completed')),
                "TASK_TITLE": todo.get('title')
            })

    print(f"Data exported to {filename}")

def get_todo_list_progress(user_id):
    """
    Fetch and display the TODO list progress for a given user.
    Also, export the data to a CSV file.

    Args:
    - user_id (int): The ID of the user.

    Returns:
    - None
    """
    # Fetch user information
    user_res = requests.get(f'{API_URL}/users/{user_id}')

    if user_res.status_code == 200:
        user_data = user_res.json()
        user_name = user_data.get('username')

        # Fetch user's TODO list
        todos_res = requests.get(f'{API_URL}/todos?userId={user_id}')

        if todos_res.status_code == 200:
            todos_data = todos_res.json()
            
            # Display TODO list progress
            print(f"Employee {user_data['name']} is done with tasks"
                  f"({user_id}/{len(todos_data)}):")

            # Display completed tasks
            for todo in todos_data:
                print(f"\t{'[x]' if todo['completed'] else '[ ]'} {todo['title']}")

            # Export data to CSV
            write_to_csv(user_id, user_name, todos_data)
        else:
            print(f"Failed to fetch TODO list. Status code: {todos_res.status_code}")
    else:
        print(f"Failed to fetch user information. Status code: {user_res.status_code}")

if __name__ == '__main__':
    # Check if command line arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    # Check if the argument is a valid user ID
    if sys.argv[1].isdigit():
        user_id = int(sys.argv[1])
        get_todo_list_progress(user_id)
    else:
        print('Invalid user ID format.')
