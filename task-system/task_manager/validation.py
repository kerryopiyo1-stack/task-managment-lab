"""
Validation module for task management system
Provides functions to validate task details
"""

from datetime import datetime

def validate_task_title(title):
    """
    Validate the task title.

    Args:
        title (str): The task title to validate

    Raises:
        ValueError: If title is invalid
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string")

    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty")

    if len(title) > 100:
        raise ValueError("Title cannot exceed 100 characters")

def validate_task_description(description):
    """
    Validate the task description.

    Args:
        description (str): The task description to validate

    Raises:
        ValueError: If description is invalid
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string")

    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty")

    if len(description) > 500:
        raise ValueError("Description cannot exceed 500 characters")

def validate_due_date(due_date):
    """
    Validate the task due date.
    Checks if the date is in the format YYYY-MM-DD

    Args:
        due_date (str): The due date to validate

    Raises:
        ValueError: If due date is invalid
    """
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string")

    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")
    
    # Check format YYYY-MM-DD
    parts = due_date.split('-')
    if len(parts) != 3:
        raise ValueError("Due date must be in format YYYY-MM-DD")

    try:
        year, month, day = parts
        year = int(year)
        month = int(month)
        day = int(day)
        
        # Validate ranges
        if year < 1900 or year > 2100:
            raise ValueError("Year must be between 1900 and 2100")
        
        if month < 1 or month > 12:
            raise ValueError("Month must be between 01 and 12")
        
        if day < 1 or day > 31:
            raise ValueError("Day must be between 01 and 31")
    except ValueError as e:
        if "between" in str(e):
            raise
        raise ValueError("Due date must contain valid numbers in format YYYY-MM-DD")