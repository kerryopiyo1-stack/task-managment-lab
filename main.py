from task_manager.validation import validate_description


tasks = []


def add_task():
    title = input()
    description = input()
    due_date = input()

    try:
        validate_description(description)
    except ValueError as error:
        print(error)
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_complete():
    if len(tasks) == 0:
        return

    try:
        task_number = int(input())
    except ValueError:
        return

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete!")


def view_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {status}")


while True:
    choice = input()

    if choice == "1":
        add_task()
    elif choice == "2":
        mark_task_complete()
    elif choice == "3":
        view_tasks()
    elif choice == "5":
        break
