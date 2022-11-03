"""Test solution for exercise 1.3."""

from sicp.chapter1.exercises.exercise_1_3 import bigest_two_sum_of_squares, bigest_two_sum_of_squares_v2
from sicp.chapter1.src.part_1_1_4 import sum_of_squares

expected = sum_of_squares(8, 10)


def test_bigest_two_sum_of_squares():
    """Test bigest_two_sum_of_squares function."""
    assert expected == bigest_two_sum_of_squares(8, 10, 3)
    assert expected == bigest_two_sum_of_squares(8, 3, 10)
    assert expected == bigest_two_sum_of_squares(3, 8, 10)
    assert expected == bigest_two_sum_of_squares(8, 8, 10)


def test_bigest_two_sum_of_squares_v2():
    """Test bigest_two_sum_of_squares_v2 function."""
    assert expected == bigest_two_sum_of_squares_v2(8, 10, 3)
    assert expected == bigest_two_sum_of_squares_v2(8, 3, 10)
    assert expected == bigest_two_sum_of_squares_v2(3, 8, 10)
    assert expected == bigest_two_sum_of_squares_v2(8, 8, 10)
