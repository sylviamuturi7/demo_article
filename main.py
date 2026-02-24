# Import functions from task_manager.task_utils package
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks,
)


# Define the main function

def main():
    while True:
        print("\nTask Management System")
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
            add_task(title, description, due_date, tasks)

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available to mark as complete.")
            else:
                for idx, t in enumerate(tasks):
                    status = "Done" if t.get("completed", False) else "Pending"
                    print(f"{idx}: {t['title']} - {status}")
                try:
                    index = int(input("Enter the index of the task to mark complete: "))
                    # Convert user-friendly 1-based input to 0-based index
                    index = index - 1
                except ValueError:
                    print("Error: Please enter a valid integer index.")
                else:
                    mark_task_as_complete(index, tasks)

        elif choice == "3":
            pending = view_pending_tasks(tasks)
            if len(pending) == 0:
                print("No pending tasks.")

        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress:.2f}%")

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
