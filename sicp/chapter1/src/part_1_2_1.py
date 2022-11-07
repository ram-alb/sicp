"""Code from part 1.2.1 of chapter1."""


def factorial(num):
    """
    Calculate factorial of number.

    Args:
        num: number

    Returns:
        number
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)


def factorial_iter(product, counter, num):
    """
    Calculate factorial of num through iter process.

    Args:
        product: number
        counter: number
        num: number

    Returns:
        number
    """
    if counter > num:
        return product
    return factorial_iter(product * counter, counter + 1)


def factorial2(num):
    """
    Calculate factorial of number.

    Args:
        num: number

    Returns:
        number
    """
    return factorial_iter(1, 1, num)
