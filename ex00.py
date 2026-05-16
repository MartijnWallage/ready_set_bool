def adder(a: int, b: int) -> int:
    """
    Bitwise addition.
    Time complexity : O(logn)
    Space complexity : O(n) (in-place)
    """
    while b > 0:
        a, b = a ^ b, (a & b) << 1
    return a


# For testing:
import operator
from utils import check


def main():
    pairs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 1),
        (101, 23),
        (12, 123),
    ]
    for pair in pairs:
        result = adder(*pair)
        expected = operator.add(*pair)
        check(result == expected, f"Expected {expected}, got {result}")


if __name__ == "__main__":
    main()
