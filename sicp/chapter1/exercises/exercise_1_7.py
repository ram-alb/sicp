"""Solution for exerceise 1.7."""

from sicp.chapter1.src.part_1_1_6 import sicp_abs
from sicp.chapter1.src.part_1_1_7 import improve


def is_good_enough(improved_guess, guess):
    """
    Check if guess is good enough.

    Args:
        improved_guess: number
        guess: number

    Returns:
        number
    """
    max_allowed_error = 0.001
    return sicp_abs(guess - improved_guess) < max_allowed_error


def sqrt_iter(improved_guess, guess, num):
    """
    Calculate the square root from a number in iter process.

    Args:
        improved_guess: number
        guess: number
        num: number

    Returns:
        number
    """
    if is_good_enough(improved_guess, guess):
        return improved_guess
    return sqrt_iter(improve(improved_guess, num), improved_guess, num)


def sqrt(num):
    """
    Calculate the square root from a number.

    Args:
        num: number

    Returns:
        number
    """
    return sqrt_iter(1, 0, num)
