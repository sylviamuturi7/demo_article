from datetime import datetime
# Import validation functions
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list
tasks = []


# Implement add_task function

def add_task(title, description, due_date, tasks_ref=tasks):
    # Validate inputs
    if not (validate_task_title(title) and
            validate_task_description(description) and
            validate_due_date(due_date)):
        return False

    # Create task dictionary
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,  # already validated format
        "completed": False,
    }

    # Append to tasks list
    tasks_ref.append(task)
    print("Task added successfully!")
    return True


# Implement mark_task_as_complete function

def mark_task_as_complete(index, tasks_ref=tasks):
    # Validate index range
    if not isinstance(index, int) or index < 0 or index >= len(tasks_ref):
        print("Error: Invalid task index.")
        return False

    tasks_ref[index]["completed"] = True
    print("Task marked as complete!")
    return True


# Implement view_pending_tasks function

def view_pending_tasks(tasks_ref=tasks):
    pending = [t for t in tasks_ref if not t.get("completed", False)]
    for i, t in enumerate(pending, start=1):
        print(f"{i}. {t['title']} (Due: {t['due_date']}) - {t['description']}")
    return pending


# Implement calculate_progress function

def calculate_progress(tasks_ref=tasks):
    total = len(tasks_ref)
    if total == 0:
        progress = 0.0
    else:
        completed = sum(1 for t in tasks_ref if t.get("completed", False))
        progress = (completed / total) * 100.0
    return progress
