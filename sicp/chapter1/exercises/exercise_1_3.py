"""Solution for exerceise 1.3."""

from sicp.chapter1.src.part_1_1_4 import sum_of_squares


def bigest_two_sum_of_squares(num1, num2, num3):
    """
    Exercise 1.3 solution.

    Args:
        num1: number
        num2: number
        num3: number

    Returns:
        number
    """
    if num1 > num3 and num2 > num3:
        return sum_of_squares(num1, num2)
    elif num1 > num2 and num3 > num2:
        return sum_of_squares(num1, num3)
    return sum_of_squares(num2, num3)


def bigest_two_sum_of_squares_v2(num1, num2, num3):
    """
    Exercise 1.3 solution version 2.

    Args:
        num1: number
        num2: number
        num3: number

    Returns:
        number
    """
    max1 = max(num1, num2)
    max2 = max(min(num1, num2), num3)
    return sum_of_squares(max1, max2)
