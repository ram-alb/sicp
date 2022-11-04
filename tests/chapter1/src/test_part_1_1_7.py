"""Test functions from chapter1.src.part_1_1_7 module."""

from math import sqrt as math_sqrt
import pytest
from sicp.chapter1.src.part_1_1_7 import sqrt


def test_sqrt():
    """Test sqrt function."""

    assert math_sqrt(1) == sqrt(1)
    assert round(math_sqrt(4)) == round(sqrt(4))
    assert round(math_sqrt(21), 2) == round(sqrt(21), 2)
    assert round(math_sqrt(10000)) == round(sqrt(10000))
    assert round(math_sqrt(0.9), 2) == round(sqrt(0.9), 2)


def test_sqrt_raises():
    """Test if sqrt function does not work with tiny numbers."""
    with pytest.raises(AssertionError):
        assert round(math_sqrt(0.0001), 2) == round(sqrt(0.0001), 2)