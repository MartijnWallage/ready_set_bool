def eval_set(formula: str, sets: list[list[int]]) -> list[int]:
    """ Each variable in formula corresponds to a list in sets.
        We use a stack with multiple sets, reduced to 1 set
        in the end.
    """
    universe = {num for s in sets for num in s}
    stack: list[set[int]] = []
    for ch in formula:
        if ch.isupper():
            i = ord(ch) - ord('A')
            stack.append(set(sets[i]))
        elif ch == '!':
            op = stack.pop()
            stack.append(universe - op)
        elif ch == '&':
            right, left = stack.pop(), stack.pop()
            stack.append(left & right)
        elif ch == '|':
            right, left = stack.pop(), stack.pop()
            stack.append(left | right)
        elif ch == '^':
            right, left = stack.pop(), stack.pop()
            stack.append((left | right) - (left & right))
        elif ch == '>':
            right, left = stack.pop(), stack.pop()
            stack.append((universe - left) | right)
        elif ch == '=':
            right, left = stack.pop(), stack.pop()
            stack.append((left & right) | (universe - (left | right)))
    if len(stack) != 1:
        raise ValueError(f"Stack invalid: {stack!r}")

    return sorted(stack.pop())


from utils import check


def main() -> None:
    sets = [
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
        [9],
    ]

    cases = [
        ("AB&", [4, 5]),
        ("AB|", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("AB^", [1, 2, 3, 6, 7, 8]),
        ("A!", [6, 7, 8, 9]),
        ("B!", [1, 2, 3, 9]),
        ("AB>", [4, 5, 6, 7, 8, 9]),
        ("AB=", [4, 5, 9]),
        ("AB&!", [1, 2, 3, 6, 7, 8, 9]),
        ("ABC||!", []),
    ]

    for i, s in enumerate(sets):
        var = chr(i + ord("A"))
        print(f"{var} = {s}")

    print("---")
    for case in cases:
        result = eval_set(case[0], sets)
        expected = case[1]
        check(result == expected,
              f"For {case[0]}, expected {expected}, got {result}")


if __name__ == "__main__":
    main()
