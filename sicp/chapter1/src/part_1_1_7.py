"""Code from part 1.1.4 of chapter1."""

from sicp.chapter1.src.part_1_1_4 import square
from sicp.chapter1.src.part_1_1_6 import sicp_abs


def average(num1, num2):
    """
    Calculate average for two numbers.

    Args:
        num1: number
        num2: number

    Returns:
        number
    """
    return (num1 + num2) / 2


def improve(guess, num):
    """
    Improve guess for better value to be a square root of num.

    Args:
        guess: number
        num: number

    Returns:
        number
    """
    return average(guess, num / guess)


def is_good_enough(guess, num):
    """
    Check if guess is good enough to be square root of a num.

    Args:
        guess: number
        num: number

    Returns:
        boolean
    """
    max_allowed_error = 0.001
    return sicp_abs(square(guess) - num) < max_allowed_error


def sqrt_iter(guess, num):
    """
    Retrun the guess if it is good enough to be square root of a num.

    Args:
        guess: number
        num: number

    Returns:
        number
    """
    if is_good_enough(guess, num):
        return guess

    return sqrt_iter(improve(guess, num), num)


def sqrt(num):
    """
    Calculate the square root of a number.

    Args:
        num: number

    Returns:
        number
    """
    return sqrt_iter(1, num)
