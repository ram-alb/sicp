"""Test functions from chapter1.src.part_1_2_2 module."""

from sicp.chapter1.src.part_1_2_2 import fib, fib2, count_change


fib0 = 0
fib1 = 1
fib10 = 55
fib20 = 6765


def test_fib():
    """Test fib function."""
    assert fib(0) == fib0
    assert fib(1) == fib1
    assert fib(10) == fib10


def test_fib2():
    """Test fib2 function."""
    assert fib2(0) == fib0
    assert fib2(1) == fib1
    assert fib2(10) == fib10


def test_count_change():
    """Test count_change function."""
    assert count_change(100) == 292
