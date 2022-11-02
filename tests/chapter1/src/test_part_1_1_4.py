"""Test functions from chapter1.src.part_1_1_4 module."""

from sicp.chapter1.src.part_1_1_4 import square, sum_of_squares


def test_square():
    """Test square function."""

    assert 1 * 1 == square(1)
    assert 5 * 5 == square(5)
    assert 9 * 9 == square(9)


def test_sum_of_squares():
    """Test sum_of_squares function."""

    assert square(3) + square(4) == sum_of_squares(3, 4)
    assert square(1) + square(1) == sum_of_squares(1, 1)