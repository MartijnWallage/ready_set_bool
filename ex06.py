from ex05 import Node, Var, Not, And, Or, to_tree, to_nnf

def distribute(l: Node, r: Node) -> Node:
    match (l, r):
        # (A & B) | C => (A | C) & (B | C)
        case (And(ll, lr), _):
            return And(distribute(ll, r), distribute(lr, r))
        # A | (B & C) => (A | B) & (A | C)
        case (_, And(rl, rr)):
            return And(distribute(l, rl), distribute(l, rr))
        case _:
            return Or(l, r)


def to_cnf(node: Node) -> Node:
    match node:
        case And(l, r):
            return (And(to_cnf(l), to_cnf(r)))
        case Or(l, r):
            return distribute(to_cnf(l), to_cnf(r))
        case _:
            return node


def to_rpn(node: Node) -> str:
    """ Walk through the tree to create a string.
        Any ampersands on a left branch have to be moved to the end 
        of the string to preserve cnf according to the subject.
    """
    match node:
        case Var(ch):
            return ch
        case Not(op):
            return to_rpn(op) + "!"
        case And(left, right): 
            new_left = to_rpn(left)
            stripped = new_left.rstrip("&")
            return stripped + to_rpn(right) + new_left[len(stripped):] + "&"
        case Or(left, right):
            return to_rpn(left) + to_rpn(right) + "|"
        case _:
            raise ValueError(f"Invalid node: {node!r}")


def conjunctive_normal_form(formula: str) -> str:
    """ Convert reverse polish notation (rpn) string to tree
        Convert tree to negation normal form (nnf).
        Convert nnf to cnf.
        Convert cnf tree back to rpn string to return.
    """
    tree = to_tree(formula)
    nnf = to_nnf(tree)
    cnf = to_cnf(nnf)
    rpn = to_rpn(cnf)
    return rpn


# For testing
from utils import check

def main():
    cases = [
        ("AB&!", "A!B!|"),
        ("AB|!", "A!B!&"),
        ("AB|C&", "AB|C&"),
        ("AB&C|", "AC|BC|&"),
        ("AB|C|D|", "AB|C|D|"),
        ("AB&C&D&", "ABCD&&&"),
        ("AB&!C!|", "A!B!|C!|"),
        ("AB|!C!&", "A!B!C!&&"),
        ("AB&CD&|", "AC|AD|BC|BD|&&&"),
        ("ABC&&DE&|", "AD|AE|BD|BE|CD|CE|&&&&&"),
        ("ABC&&DE&|!", "A!B!C!||D!E!|&"),
    ]

    for case in cases:
        result = conjunctive_normal_form(case[0])
        expected = case[1]
        check(result == expected, f"For {case[0]}, expected {expected}, got {result}")


if __name__ == "__main__":
    main()

