"""Test solution for exercise 1.8."""

from sicp.chapter1.exercises.exercise_1_8 import cube_root


def test_cube_root():
    """Test cube_root function."""

    assert round(cube_root(0)) == 0
    assert round(cube_root(1)) == 1
    assert round(cube_root(8)) == 2
    assert round(cube_root(1000)) == 10
    assert round(cube_root(-1000)) == -10
    assert round(cube_root(0.125), 1) == 0.5
