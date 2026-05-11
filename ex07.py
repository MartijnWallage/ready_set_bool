from ex04 import eval_formula, make_assignments

def sat(formula: str) -> bool:
    """ Since we only need O(2^n), we simply try out all assignments
        evaluate the formula with each assignment
        return true iff any eval is true:
    """
    assignments = make_assignments(formula)
    return any(assignment for assignment in assignments if eval_formula(formula, assignment))


def main():
    cases = [
        "AB&",
        "AB|",
        "AB!&",
        "AB^",
        "A!A&",
        "AB|A!B!&&",
    ]

    for case in cases:
        print(f"{case}: {sat(case)}")


if __name__ == "__main__":
    main()
