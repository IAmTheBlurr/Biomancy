""" This module contains utility functions for the biomancy package. """


def to_bool(string: str) -> bool:
    """
    Convert a string to a boolean. Only accepts 'true' or 'false' as input.

    Args:
        string (str): The string to convert to a boolean.

    Returns:
        bool: The boolean representation of the string.

    """
    lowered = string.lower()
    if lowered not in ['true', 'false']:
        raise ValueError(f'This method only accepts "true" or "false" as input. Received: {string}')

    return True if lowered == 'true' else False
