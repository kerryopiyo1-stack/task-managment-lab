from task_manager.task_utils import (
    add_task,
    calculate_progress,
    mark_task_as_complete,
    view_pending_tasks,
)


tasks = []


def display_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks found.")
        return

    for index, task in enumerate(task_list, start=1):
        status = "Complete" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {task['description']} - {task['due_date']} - {status}")


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            try:
                add_task(tasks, title, description, due_date)
                print("Task added successfully!")
            except ValueError as error:
                print(error)
        elif choice == "2":
            display_tasks(tasks)
            task_number = input("Enter task number to mark as complete: ")

            try:
                mark_task_as_complete(tasks, int(task_number) - 1)
                print("Task marked as complete!")
            except ValueError as error:
                print(error)
        elif choice == "3":
            pending_tasks = view_pending_tasks(tasks)
            display_tasks(pending_tasks)
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
