def calculate_progress(tasks):
    """
    Calculate percentage of completed tasks.
    """
    if len(tasks) == 0:
        print(0)
        return

    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100

    print(progress)