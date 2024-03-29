#!/usr/bin/python3
"""Python script that returns information about a given employee ID"""
import re
import requests
import sys

"""The API's URL"""
API_URL = 'https://jsonplaceholder.typicode.com'

"""Check if the script is being run directly"""
if __name__ == '__main__':
    """Checks if command line arguments were provided"""
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            """Gets the user's information from the API"""
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('name')

            """Filter todos for the given user"""
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))

            """Print the user's tasks"""
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
