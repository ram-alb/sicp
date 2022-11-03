"""Code from part 1.1.4 of chapter1."""


def sicp_abs(num):
    """
    Calculate the modulus of a number.

    Args:
        num: number

    Returns:
        number
    """
    if num < 0:
        return -num
    return num
