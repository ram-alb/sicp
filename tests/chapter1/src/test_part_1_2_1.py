"""Test functions from chapter1.src.part_1_2_1 module."""

from sicp.chapter1.src.part_1_2_1 import factorial


def test_factorial():
    """Test factorial function."""
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial2():
    """Test factorial2 function."""
    assert factorial(1) == 1
    assert factorial(5) == 120