def gray_code(n: int) -> int:
    return n ^ (n >> 1)


# For testing
from utils import check


def main() -> None:
    last = 0
    result = gray_code(last)
    check(result == 0, f"For gray code of 0, got {result:>8b}")
    for i in range(1, 100):
        result = gray_code(i)
        difference = result ^ last
        # Difference from last must have only one positive digit
        check(difference & (difference - 1) == 0,
              f"For gray code of {i}, got {result:>8b}")
        last = result


if __name__ == "__main__":
    main()
