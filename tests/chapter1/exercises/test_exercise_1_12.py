"""Test solution for exercise 1.12."""

from sicp.chapter1.exercises.exercise_1_12 import pascal


def test_pascal():
    """Test pascal function."""
    assert pascal(1, 1) == 1
    assert pascal(4, 1) == 1
    assert pascal(4, 4) == 1
    assert pascal(5, 2) == 4
    assert pascal(5, 3) == 6
