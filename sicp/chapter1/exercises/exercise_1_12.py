"""Solution for exercise 1.11."""


def pascal(row, col):
    """
    Calculate element in pascal triangle by position.

    Args:
        row: number
        col: number

    Returns:
        number
    """
    if col in {row, 1}:
        return 1
    new_row = row - 1
    return pascal(new_row, col - 1) + pascal(new_row, col)
