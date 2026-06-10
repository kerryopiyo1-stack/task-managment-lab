from datetime import datetime

# Import validation functions
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid task title.")
        return

    if not validate_task_description(description):
        print("Invalid task description.")
        return

    if not validate_due_date(due_date):
        print("Invalid due date. Use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")
    
# Implement view_pending_tasks function
def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending, start=1):
        print(
            f"{i}. {task['title']} - {task['description']} "
            f"(Due: {task['due_date']})"
        )

# Implement calculate_progress function
def calculate_progress(tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = sum(1 for task in tasks if task["completed"])
        progress = (completed / len(tasks)) * 100

    return progress