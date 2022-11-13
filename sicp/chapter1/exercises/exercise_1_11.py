"""Solution for exercise 1.11."""


def func(num):
    """
    Calculate the answer for a number according to a function definition.

    Args:
        num: number

    Returns:
        number
    """
    if num < 3:
        return num

    return func(
        num - 1,
    ) + func(
        num - 2,
    ) + func(
        num - 3,
    )


def func_iter(acc1, acc2, acc3, counter):
    """
    Calculate the answer for a number according to a function definition in iter process.

    Args:
        acc1: number
        acc2: number
        acc3: number
        counter: number

    Returns:
        number
    """
    if counter == 0:
        return acc3
    return func_iter(acc1 + acc2 + acc3, acc1, acc2, counter - 1)


def func2(num):
    """
    Calculate the answer for a number according to a function definition.

    Args:
        num: number

    Returns:
        number
    """
    return func_iter(2, 1, 0, num)
