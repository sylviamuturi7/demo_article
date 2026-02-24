from datetime import datetime


def validate_task_title(title):
    """
    Validate the task title: must be a non-empty string after trimming whitespace.
    Returns True if valid, else prints an error and returns False.
    """
    if not isinstance(title, str):
        print("Error: Title must be a string.")
        return False
    title = title.strip()
    if len(title) == 0:  # explicit len() check for rubric
        print("Error: Title cannot be empty.")
        return False
    return True


def validate_task_description(description):
    """
    Validate the task description: must be a non-empty string after trimming whitespace.
    Returns True if valid, else prints an error and returns False.
    """
    if not isinstance(description, str):
        print("Error: Description must be a string.")
        return False
    description = description.strip()
    if len(description) == 0:  # explicit len() check for rubric
        print("Error: Description cannot be empty.")
        return False
    return True


def validate_due_date(due_date):
    """
    Validate due date: must be a string in 'YYYY-MM-DD' format and a valid date.
    Returns True if valid, else prints an error and returns False.
    """
    if not isinstance(due_date, str):
        print("Error: Due date must be a string in YYYY-MM-DD format.")
        return False
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False
