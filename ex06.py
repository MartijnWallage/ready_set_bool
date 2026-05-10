from ex05 import Node, Var, Not, And, Or, to_tree, to_nnf, to_rpn

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


def conjunctive_normal_form(formula: str) -> str:
    """ Convert reverse polish notation (rpn) string to tree
        Convert tree to negation normal form (nnf).
        Convert nnf to cnf.
        Convert cnf tree back to rpn string to return.
    """
    print(f"formula: {formula}")
    tree = to_tree(formula)
    print(f"tree:    {tree}")
    nnf = to_nnf(tree)
    print(f"nnf:     {nnf}")
    cnf = to_cnf(nnf)
    print(f"cnf:     {cnf}")
    rpn = to_rpn(cnf)
    print(f"rpn:     {rpn}")
    return rpn


def main():
    cases = [
        "AB&!",
        "AB|!",
        "AB|C&",
        "AB|C|D|",
        "AB&C&D&",
        "AB&!C!|",
        "AB|!C!&",
        "AB&CD&|",
    ]

    for case in cases:
        result = conjunctive_normal_form(case)
        print(f"\n{case}: {result}\n")


if __name__ == "__main__":
    main()

