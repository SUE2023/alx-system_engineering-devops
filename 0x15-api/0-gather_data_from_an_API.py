#!/usr/bin/python3
"""
Script to get TODO list progress for a given employee ID using REST API.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """ Base URL for the API"""
    base_url = "https://jsonplaceholder.typicode.com"
    
    """ Fetch employee details """
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    """Fetch TODO list for the employee"""
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    """ Gets employee name"""
    employee_name = user_data.get("name")
    
    """Calculate TODO list progress"""
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    
    """ Print the result"""
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)

