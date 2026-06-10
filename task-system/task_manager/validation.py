def validate_description(description):
    """
    Validate task description length.
    """
    if len(description) > 500:
        raise ValueError("Description cannot exceed 500 characters")

    return True