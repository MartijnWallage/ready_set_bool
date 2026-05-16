def eval_formula(formula: str) -> bool:
    """
    Evaluate formula in boolean logic, reversed polish notation.
    0 for True and 1 for False. No variables.
    Time complexity: n (simple loop through the chars of formula)
    """
    stack: list[bool] = []
    for ch in formula:
        if ch == '0':
            stack.append(False)
        elif ch == '1':
            stack.append(True)
        elif ch == '!':
            a = stack.pop()
            stack.append(not a)
        elif ch == '&':
            right, left = stack.pop(), stack.pop()
            stack.append(left and right)
        elif ch == '|':
            right, left = stack.pop(), stack.pop()
            stack.append(left or right)
        elif ch == '^':
            right, left = stack.pop(), stack.pop()
            stack.append(left != right)
        elif ch == '>':
            right, left = stack.pop(), stack.pop()
            stack.append(not left or right)
        elif ch == '=':
            right, left = stack.pop(), stack.pop()
            stack.append(left == right)
        else:
            raise ValueError(f"Unknown symbol: {ch!r}")

    if len(stack) != 1:
        raise ValueError(f"Invalid formula: {stack}")
    return stack.pop()


# For testing
from utils import check


def main():
    cases = [
        ("10&", False),
        ("10|", True),
        ("10|1&", True),
        ("101|&", True),
        ("1", True),
        ("0", False),
        ("00|", False),
        ("001||", True),
        ("001|&", False),
        ("0!", True),
        ("1!", False),
        ("11^", False),
        ("10^", True),
        ("01^", True),
        ("00^", False),
        ("01>", True),
        ("10>", False),
        ("0!0>", False),
        ("11=", True),
        ("1!0=", True),
        ("0!0=", False),
        ("10|1>", True),
    ]
    for case in cases:
        result = eval_formula(case[0])
        expected = case[1]
        check(result == expected,
              f"For {case[0]}, expected {expected}, got {result}")


if __name__ == "__main__":
    main()
