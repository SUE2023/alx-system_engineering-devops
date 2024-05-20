#!/usr/bin/python3
"""
Script to get TODO list progress for all employees using REST API
and export the data to a JSON file.
"""
import json
import requests

def get_all_todo_progress():
    """ Base URL for the API"""
    base_url = "https://jsonplaceholder.typicode.com"
    
    """Fetch all employees details"""
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()
    
    """Prepare a dictionary to store all tasks from all employees"""
    all_todos = {}
    
    """Loop through each user to get their TODO list"""
    for user in users_data:
        employee_id = user.get("id")
        employee_username = user.get("username")
        
        """Fetch TODO list for the current employee"""
        todos_url = f"{base_url}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        
        """Prepare the list of tasks for the current employee"""
        tasks = [
            {
                "username": employee_username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data
        ]
        
        """Add the tasks to the all_todos dictionary under the employee_id"""
        all_todos[employee_id] = tasks
    
    # Write data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_todos, json_file, indent=4)
    
    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    get_all_todo_progress()

