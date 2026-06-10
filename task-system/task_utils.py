	
"""
Task utilities module for task management operations
Provides functions to manage tasks, mark them complete, and track progress
"""

from .validation import validate_task_title, validate_task_description, validate_due_date

def add_task(tasks_list, title, description, due_date):
    """
    Add a new task to the tasks list after validating input.

    Args:
        tasks_list (list): List of task dictionaries
        title (str): Task title
        description (str): Task description
        due_date (str): Task due date in YYYY-MM-DD format

    Raises:
        ValueError: If validation fails
    """
    # Validate inputs
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    # Create new task
    new_task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }

    tasks_list.append(new_task)
def mark_task_as_complete(tasks_list, task_index):
    """
    Mark a task as complete.

    Args:
        tasks_list (list): List of task dictionaries
        task_index (int): Index of the task to mark as complete

    Raises:
        ValueError: If task_index is invalid
    """
    if not isinstance(task_index, int):
        raise ValueError("Task index must be an integer")

    if task_index < 0 or task_index >= len(tasks_list):
        raise ValueError("Invalid task index")

    if tasks_list[task_index]["completed"]:
        raise ValueError("Task is already completed")

    tasks_list[task_index]["completed"] = True

def view_pending_tasks(tasks_list):
    """
    View all pending (incomplete) tasks.

    Args:
        tasks_list (list): List of task dictionaries

    Returns:
        list: List of pending tasks
    """
    pending_tasks = [task for task in tasks_list if not task["completed"]]
    return pending_tasks

def calculate_progress(tasks_list):
    """
    Calculate progress percentage.

    Args:
        tasks_list (list): List of task dictionaries

    Returns:
        float: Completion percentage
    """
    if len(tasks_list) == 0:
        return 0.0

    total = len(tasks_list)
    completed = sum(1 for task in tasks_list if task["completed"])
    percentage = (completed / total) * 100

    return percentage

def get_all_tasks(tasks_list):
    """
    Get all tasks (both completed and pending).

    Args:
        tasks_list (list): List of task dictionaries

    Returns:
        list: All tasks
    """
    return tasks_list