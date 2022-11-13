"""Code from part 1.2.2 of chapter1."""


def fib(num):
    """
    Calculat Fibonacci number in recursive process.

    Args:
        num: number

    Returns:
        number
    """
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


def fib_iter(state1, state2, count):
    """
    Calculat Fibonacci number in iter process.

    Args:
        state1: number
        state2: number
        count: number

    Returns:
        number
    """
    if count == 0:
        return state2
    return fib_iter(state1 + state2, state1, count - 1)


def fib2(num):
    """
    Calculat Fibonacci number in iter process.

    Args:
        num: number

    Returns:
        number
    """
    return fib_iter(1, 0, num)


def first_denomination(kinds_of_coins):
    """
    Return first denomination coin.

    Args:
        kinds_of_coins: number

    Returns:
        number
    """
    first_denomination_values = {
        1: 1,
        2: 5,
        3: 10,
        4: 25,
        5: 50,
    }
    return first_denomination_values[kinds_of_coins]


def cc_iter(amount, kinds_of_coins):
    """
    Count the number of ways to change amount of money in recursive process.

    Args:
        amount: number
        kinds_of_coins: number

    Returns:
        number
    """
    if amount == 0:
        return 1
    if amount < 0 or kinds_of_coins == 0:
        return 0
    return cc_iter(
        amount,
        kinds_of_coins - 1,
    ) + cc_iter(
        amount - first_denomination(kinds_of_coins),
        kinds_of_coins,
    )


def count_change(amount):
    """
    Count the number of ways to change amount of money in recursive process.

    Args:
        amount: number

    Returns:
        number
    """
    return cc_iter(amount, 5)
