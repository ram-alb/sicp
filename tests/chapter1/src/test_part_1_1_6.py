"""Test functions from chapter1.src.part_1_1_6 module."""

from sicp.chapter1.src.part_1_1_6 import sicp_abs


def test_sicp_abs():
    """Test sicp_abs function."""

    assert sicp_abs(-5) == 5
    assert sicp_abs(0) == 0
    assert sicp_abs(5) == 5
