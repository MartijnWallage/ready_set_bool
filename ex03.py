def eval_formula(formula: str) -> bool:
    stack: list[bool] = []
    for ch in formula:
        if ch == '0': stack.append(False)
        elif ch == '1': stack.append(True)
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
        else: raise ValueError(f"Unknown symbol: {ch!r}")

    if len(stack) != 1:
        raise ValueError(f"Invalid formula: {stack}")
    return stack.pop()


def main():
    cases = [
        "10&",
        "10|",
        "10|1&",
        "101|&",
    ]
    for case in cases:
        print(f"{case}: {eval_formula(case)}")


if __name__ == "__main__":
    main()
