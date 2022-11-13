"""Test solution for exercise 1.11."""

from sicp.chapter1.exercises.exercise_1_11 import func, func2


def test_func():
    """Test func function."""
    assert func(1) == 1
    assert func(2) == 2
    assert func(5) == 11
    assert func(8) == 68


def test_func2():
    """Test func function."""
    assert func2(1) == 1
    assert func2(2) == 2
    assert func2(5) == 11
    assert func2(8) == 68
