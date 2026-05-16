from ex00 import adder


def multiplier(a: int, b: int) -> int:
    """
    Bitwise multiplication.
    Subject says time and space complexity should be O(1).
    But that makes no sense: time and space needed for
    multiplication is obviously dependent on the size of the input.
    Actual time complexity: O(logn)
    Space complexity: O(n)
    """
    result = 0
    i = 0
    while b >> i > 0:
        if (b >> i) & 1:
            result = adder(result, a << i)
        i += 1
    return result


# For testing
import operator
from utils import check


def main():
    cases = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 1),
        (123, 13),
        (9, 132),
    ]
    for case in cases:
        result = multiplier(*case)
        expected = operator.mul(*case)
        check(result == expected, f"Expected {expected}, got {result}")


if __name__ == "__main__":
    main()
