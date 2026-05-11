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


def main():
    formulas = [
        "AB&",
        "AB|",
        "AB^",
        "A!",
        "B!",
        "AB>",
        "AB=",
    ]

    sets = [
        [1,2,3,4,5],
        [4,5,6,7,8],
        [9],
    ]

    for i, s in enumerate(sets):
        var = chr(i + ord("A"))
        print(f"{var} = {s}")

    print("---")
    for formula in formulas:
        print(f"{formula}: {eval_set(formula, sets)}")


if __name__ == "__main__":
    main()
