def eval_formula(formula: str, assignment: dict[str, bool]) -> bool:
    """
    Evaluate formula in boolean logic, reversed polish notation,
    under a truth value assignment to variables.
    """
    stack: list[bool] = []
    for ch in formula:
        if ch.isupper():
            stack.append(assignment[ch])
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


def make_assignments(formula: str) -> list[dict[str, bool]]:
    """
    Create table of assignments using sequence of binary numbers.
    Separated from print_truth_table because useful for later exercise.
    """
    vars = sorted({ch for ch in formula if ch.isupper()})
    assignments: list[dict[str, bool]] = []
    n = len(vars)
    for i in range(1 << n):
        assignment: dict[str, bool] = {}
        for j, var in enumerate(vars):
            # i is the number we want to map onto each variable
            # j is the digit of that number.
            # For example, A should get the value of the 0th digit of i
            # B the value of the 1st digit of i
            shift = len(vars) - 1 - j
            assignment[var] = bool(i >> shift & 1)
        assignments.append(assignment)
    return assignments


def print_truth_table(formula: str):
    """
    Print truth table for formula in reversed polish notation.
    """
    vars = sorted({ch for ch in formula if ch.isupper()})
    header = "| " + " | ".join(vars) + " | = |"
    sep = "|-" + "-|-".join("-" for _ in vars) + "-|---|"
    print(header)
    print(sep)

    assignments = make_assignments(formula)
    for assignment in assignments:
        for var in vars:
            print(f"| {int(assignment[var])} ", end="")
        print(f"| {int(eval_formula(formula, assignment))} |")


def main():
    """
    Test print truth table.
    """
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
