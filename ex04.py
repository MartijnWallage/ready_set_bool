def eval_formula(formula: str, assignment: dict[str, bool]) -> bool:
    stack: list[bool] = []
    for ch in formula:
        if ch.isupper(): stack.append(assignment[ch])
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


def print_truth_table(formula: str):
    vars = [ch for ch in formula if ch.isupper()]
    vars.sort()
    assignments: list[dict[str, bool]] = []
    i = 0
    n = pow(2, len(vars))
    while i < n:
        assignment: dict[str, bool] = {}
        for j, var in enumerate(vars):
            # i is the number we want to map onto each variable
            # j is the digit of that number.
            # For example, A should get the value of the 0th digit of i
            # B the value of the 1st digit of i
            assignment[var] = (i >> (len(vars) - 1 - j)) & 1
        assignments.append(assignment)
        i += 1

    print("|", end="")
    for var in vars:
        print(f" {var} |", end="")
    print(" = |")
    for _ in range(len(vars)+1):
        print("|---", end="")
    print("|")
    for assignment in assignments:
        for var in vars:
            print(f"| {int(assignment[var])} ", end="")
        print(f"| {int(eval_formula(formula, assignment))} |")


def main():
    cases = [
        "AB^",
        "AB&",
        "AB>",
        "A!BC&>",
        "AB&C|",
    ]
    for case in cases:
        print(case)
        print_truth_table(case)
        print()


if __name__ == "__main__":
    main()

