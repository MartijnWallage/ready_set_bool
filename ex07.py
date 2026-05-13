from ex04 import eval_formula, make_assignments

def sat(formula: str) -> bool:
    """ Since we only need O(2^n), we simply try out all assignments
        evaluate the formula with each assignment
        return true iff any eval is true:
    """
    assignments = make_assignments(formula)
    return any(assignment for assignment in assignments if eval_formula(formula, assignment))


from utils import check

def main():
    cases = [
        ("A", True),
        ("AB&", True),
        ("AB|", True),
        ("AB!&", True),
        ("AB^", True),
        ("A!A&", False),
        ("AB|A!B!&&", False),
    ]

    for case in cases:
        result = sat(case[0])
        expected = case[1]
        check(result == expected, f"For {case[0]}, expected {expected}, got {result}")


if __name__ == "__main__":
    main()
