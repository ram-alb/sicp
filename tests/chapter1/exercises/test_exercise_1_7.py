"""Test solution for exercise 1.7."""

from math import sqrt as math_sqrt
from sicp.chapter1.exercises.exercise_1_7 import sqrt


def test_sqrt():
    """Test sqrt function."""

    assert math_sqrt(1) == sqrt(1)
    assert round(math_sqrt(0)) == round(sqrt(0))
    assert round(math_sqrt(4)) == round(sqrt(4))
    assert round(math_sqrt(21), 2) == round(sqrt(21), 2)
    assert round(math_sqrt(10000)) == round(sqrt(10000))
    assert round(math_sqrt(0.9), 2) == round(sqrt(0.9), 2)
    assert round(math_sqrt(0.0001), 2) == round(sqrt(0.0001), 2)
    assert round(math_sqrt(10000000000000), 2) == round(sqrt(10000000000000), 2)
