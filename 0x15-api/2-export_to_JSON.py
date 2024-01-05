#!/usr/bin/python3
'''A Python script to export data in the JSON format'''

import json
import re
import requests
import sys

"""The base URL of the JSONPlaceholder API"""
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """
    Check if command line arguments were provided and proceed accordingly.
    """
    if len(sys.argv) > 1:
        """
        Checks if the provided argument is a valid user ID (numerical).
        """
        if re.fullmatch(r'\d+', sys.argv[1]):
            """
            Extracts the user ID and convert it to an integer.
            """
            user_id = int(sys.argv[1])

            """
            Makes an API call to retrieve the user information based
            on the provided user ID.
            """
            user_data = requests.get('{}/users/{}'.format(API_URL, user_id)).json()

            """
            Makes another API call to retrieve the todos (tasks)
            associated with the user.
            """
            todos_data = requests.get('{}/todos'.format(API_URL)).json()

            """Filters the todos for the given user"""
            todos = list(filter(lambda x: x.get('userId') == user_id, todos_data))

            """Writes the data to a JSON file"""
            with open('{}.json'.format(user_id), 'w') as file:
                """
                Maps todos to the desired JSON format for better organization.
                """
                user_tasks = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': user_data.get('username')
                    },
                    todos
                ))
                user_data_formatted = {
                    '{}'.format(user_id): user_tasks
                }

                """
                Writes the structured JSON data to the file.
                """
                json.dump(user_data_formatted, file, indent=4)
