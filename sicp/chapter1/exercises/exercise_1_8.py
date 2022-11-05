"""Solution for exerceise 1.8."""

from sicp.chapter1.src.part_1_1_4 import square
from sicp.chapter1.exercises.exercise_1_7 import is_good_enough


def improve(guess, num):
    """
    Improve assumption to find cube root of a number.

    Args:
        guess: number
        num: number

    Returns:
        number
    """
    return (num / square(guess) + 2 * guess) / 3


def cube_root_iter(improved_guess, guess, num):
    """
    Calculate the cube root from a number in iter process.

    Args:
        improved_guess: number
        guess: number
        num: number

    Returns:
        number
    """
    if is_good_enough(improved_guess, guess):
        return improved_guess
    return cube_root_iter(improve(improved_guess, num), improved_guess, num)


def cube_root(num):
    """
    Calculate the cube root from a number.

    Args:
        num: number

    Returns:
        number
    """
    return cube_root_iter(1, 0, num)
