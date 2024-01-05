#!/usr/bin/python3
"""Python script that returns information about a given employee ID"""
import requests
import sys


def get_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    """Fetching user information"""
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    """Fetching user's TODO list"""
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    """Extracting completed and total tasks"""
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)
    completed_count = len(completed_tasks)

    """Displaying employee's TODO list progress"""
    print(f"Employee {user_data['name']} is done with tasks"
          f"({completed_count}/{total_tasks}):")

    """Displaying completed tasks"""
    for task in completed_tasks:
        print(f"    {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
