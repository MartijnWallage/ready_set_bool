def eval_sets(formula: str, sets: list[list[int]]) -> list[int]:
    """ Each variable in formula corresponds to a list in sets.
        We use a stack with multiple sets, reduced to 1 set 
        in the end.
    """
    universe = {num for s in sets for num in s}
    stack: list[list[int]] = []
    for ch in formula:
        if ch.isupper():
            i = ord(ch) - ord('A')
            stack.append(sets[i])
        elif ch == '!':
            op = stack.pop()
            complement = [num for num in universe if num not in op]
            stack.append(complement)
        elif ch == '&':
            right, left = stack.pop(), stack.pop()
            stack.append([num for num in universe if num in left and num in right])
        elif ch == '|':
            right, left = stack.pop(), stack.pop()
            stack.append([num for num in universe if num in left or num in right])
        elif ch == '^':
            right, left = stack.pop(), stack.pop()
            stack.append([num for num in universe if (num in left and num not in right) or (num in right and num not in left)])
        elif ch == '>':
            right, left = stack.pop(), stack.pop()
            stack.append([num for num in universe if num not in left or num in right])
        elif ch == '=':
            right, left = stack.pop(), stack.pop()
            stack.append([num for num in universe if (num not in left and num not in right) or (num in left and num in right)])

    if len(stack) != 1:
        raise ValueError(f"Stack invalid: {stack!r}")

    return stack.pop()


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
    ]

    for i, s in enumerate(sets):
        var: char = chr(i + ord("A"))
        print(f"{var} = {s}")

    print("---")
    for formula in formulas:
        print(f"{formula}: {eval_sets(formula, sets)}")


if __name__ == "__main__":
    main()
