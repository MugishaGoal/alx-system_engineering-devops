#!/usr/bin/python3
import requests
import csv
import sys


def export_to_csv(employee_id, tasks):
    """
    Export task data to a CSV file.

    Args:
    - employee_id (int): The ID of the employee.
    - tasks (list): List of tasks associated with the employee.

    Returns:
    - None
    """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": task.get("username", ""),
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

    print(f"Data exported to {filename}")


def get_todo_list_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee.
    Also, export the data to a CSV file.

    Args:
    - employee_id (int): The ID of the employee.

    Returns:
    - None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    """Fetching user information"""
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    """Fetching user's TODO list"""
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    """Displaying employee's TODO list progress"""
    print(f"Employee {user_data['name']} is done with tasks"
          f"({user_data['id']}/{len(todo_data)}):")

    """Displaying completed tasks"""
    for task in todo_data:
        print(f"\t{'[x]' if task['completed'] else '[ ]'} {task['title']}")

    """Exporting data to CSV"""
    export_to_csv(employee_id, todo_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
