from dataclasses import dataclass
from ex04 import eval_formula, make_assignments
from ex06 import conjunctive_normal_form


@dataclass
class Var:
    name: str
    sign: bool

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"{self.name}" + ("!" if not self.sign else "")


def unit_propagate(clauses: list[list[Var]], assignment: dict[str, bool]) -> bool:
    for clause in clauses:
        if len(clause) == 1:
            var = clause[0]
            if var.name in assignment and assignment[var.name] != var.sign:
                return False
            assignment[var.name] = var.sign
    return True


def pure_literal_assign(clauses: list[list[Var]], assignment: dict[str, bool]):
    trial_assign: dict[str, bool] = {}
    ban_list: set[str] = set(assignment.keys())
    for clause in clauses:
        for var in clause:
            if var.name not in ban_list:
                if var.name in trial_assign and trial_assign[var.name] != var.sign:
                    trial_assign.pop(var.name)
                    ban_list.add(var.name)
                else:
                    trial_assign[var.name] = var.sign
    assignment |= trial_assign


def simplify(clauses: list[list[Var]], assignment: dict[str, bool]):
    for clause in clauses[:]:
        for var in clause[:]:
            if var.name not in assignment:
                continue
            if assignment[var.name] == var.sign:
                clauses.remove(clause)
                break
            else:
                clause.remove(var)


def pick_next_literal(clauses: list[list[Var]], assignment: list[str, bool]) -> str:
    for clause in clauses:
        for var in clause:
            if var.name not in assignment:
                return var.name
    raise ValueError("No unassigned literal left.")


def dpll(clauses: list[list[Var]], assignment: dict[str, bool]) -> bool:
    """
    Algorithm DPLL
        Input: A set of prop Φ.
        Output: A truth value indicating whether Φ is satisfiable.
    Time complexity: worst case (no simplification possible) O(2^n), but usually better
    Space complexity: O(n)
    """
    # unit-propagate:
    if not unit_propagate(clauses, assignment):
        return False
    # pure-literal-assign:
    pure_literal_assign(clauses, assignment)
    simplify(clauses, assignment)

    # Test validity
    if clauses == []:
        return True
    for clause in clauses:
        if clause == []:
            return False

    clauses_cpy = [clause[:] for clause in clauses]  # deep copy for backtracking
    assignment_cpy = assignment.copy() # deep copy for backtracking
    next = pick_next_literal(clauses, assignment)
    return dpll(clauses, assignment | {next: True}) or dpll(clauses_cpy, assignment_cpy | {next: False})


def split_clauses(formula: str) -> list[list[Var]]:
    clauses: list[list[Var]] = []
    for ch in formula:
        if ch == "&":
            break # All the ampersands stack up at the end and can be ignored
        elif ch == "|":
            # Disjunction merges two vars into one clause
            right = clauses.pop()
            clauses[-1] += right
        elif ch == "!":
            # Negation flips the sign of the last var in the last clause
            clauses[-1][-1].sign = not clauses[-1][-1]
        elif ch.isupper():
            # A variable, until we encounter an operator, forms a clause by itself
            var: Var = Var(ch, True)
            clause = [var]
            clauses.append(clause)
        else:
            raise ValueError(f"Invalid character: {ch!r}")

    return clauses


def sat(formula: str) -> bool:
    """ The exercise only asks for O(2^n), so we could simply try each assignment.
    But we reserve that approach for testing. Here, just for fun, we implement the
    Davis-Putnam algorithm.
    """
    cnf = conjunctive_normal_form(formula)
    clauses = split_clauses(cnf)
    return dpll(clauses=clauses, assignment={})


def sat_brute_force(formula: str) -> bool:
    """ Since we only need O(2^n), we simply try out all assignments.
    """
    assignments = make_assignments(formula)
    return any(assignment for assignment in assignments if eval_formula(formula, assignment))


from utils import check

def main():
    cases = [
        "A",
        "AB&",
        "AB|",
        "AB!&",
        "AB^",
        "A!A&",
        "AB|A!B!&&",
        "ABC&&",
        "ABC||",
        "A!B!C!&&A&",
        "AB!^AD^&",
        "AB>A!B!>&",
        "AB>A!B>&BA!>&",
        "AB!>A!B>BA>&&",
        "AB>BC>CA!>A!BC!&>&&&",
    ]

    for case in cases:
        result = sat(case)
        expected = sat_brute_force(case)
        check(result == expected, f"For {case}, expected {expected}, got {result}")


if __name__ == "__main__":
    main()
