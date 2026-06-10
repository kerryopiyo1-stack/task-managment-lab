try:
    from .validation import (
        validate_due_date,
        validate_task_description,
        validate_task_title,
    )
except ImportError:
    from validation import (
        validate_due_date,
        validate_task_description,
        validate_task_title,
    )


tasks = []


def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
    except ValueError as error:
        print(error)
        return

    if not validate_due_date(due_date):
        print("Invalid due date. Use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")


def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    for index, task in enumerate(pending, start=1):
        print(f"{index}. {task['title']} - {task['description']} (Due: {task['due_date']})")


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(1 for task in tasks if task["completed"])
    return (completed / len(tasks)) * 100
