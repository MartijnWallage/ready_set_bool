class Node:
    pass


class Var(Node):
    __match_args__ = ("name",)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Var({self.name!r})"

    def __eq__(self, other):
        return instance(other, Var) and self.name == other.name


class Not(Node):
    __match_args__ = ("operand",)

    def __init__(self, operand: Node):
        self.operand = operand

    def __repr__(self):
        return f"Not({self.operand!r})"

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand


class And(Node):
    __match_args__ = ("left", "right",)

    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"And(left={self.left!r}, right={self.right!r})"

    def __eq__(self, other):
        return isinstance(other, And) and {self.left, self.right} == {other.left, other.right}


class Or:
    __match_args__ = ("left", "right",)

    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Or(left={self.left!r}, right={self.right!r})"

    def __eq__(self, other):
        return isinstance(other, Or) and {self.left, self.right} == {other.left, other.right}


def to_tree(formula: str) -> Node:
    stack: list[Node] = []

    for ch in formula:
        if ch.isupper(): stack.append(Var(ch))
        elif ch == '!': 
            operand = stack.pop()
            stack.append(Not(operand))
        elif ch == '&':
            right, left = stack.pop(), stack.pop()
            stack.append(And(left, right))
        elif ch == '|':
            right, left = stack.pop(), stack.pop()
            stack.append(Or(left, right))
        elif ch == '^':
            right, left = stack.pop(), stack.pop()
            stack.append(Or(And(left, Not(right)), And(Not(left), right)))
        elif ch == '>':
            right, left = stack.pop(), stack.pop()
            stack.append(Or(Not(left), right))
        elif ch == '=':
            right, left = stack.pop(), stack.pop()
            stack.append(Or(And(left, right), And(Not(left), Not(right))))
        else:
            raise ValueError(f"Invalid character: {ch!r}")

    if len(stack) != 1:
        raise ValueError(f"Invalid formula. Left on stack: {stack!r}")

    return stack.pop()

def to_nnf(node: Node) -> Node:
    match node:
        case Var(_):
            return node
        case Not(Var(_)): 
            return node
        case Not(Not(op)): 
            return to_nnf(op)
        case Not(And(left, right)): 
            return Or(to_nnf(Not(left)), to_nnf(Not(right)))
        case Not(Or(left, right)): 
            return And(to_nnf(Not(left)), to_nnf(Not(right)))
        case And(left, right): 
            return And(to_nnf(left), to_nnf(right))
        case Or(left, right): 
            return Or(to_nnf(left), to_nnf(right))
        case _:
            raise ValueError(f"Invalid node: {node!r}")


def to_rpn(node: Node) -> str:
    match node:
        case Var(ch):
            return ch
        case Not(op):
            return to_rpn(op) + "!"
        case And(left, right):
            return to_rpn(left) + to_rpn(right) + "&"
        case Or(left, right):
            return to_rpn(left) + to_rpn(right) + "|"
        case _:
            raise ValueError(f"Invalid node: {node!r}")


def negation_normal_form(formula: str) -> str:
    """ Convert formula to tree, already parsing > and ^
        Recursively convert tree to negation normal form (nnf).
        Convert back to string in reverse polish notation. """
    return to_rpn(to_nnf(to_tree(formula)))


def main():
    cases = [
        "AB&!",
        "AB|!",
        "AB>",
        "AB=",
        "AB|C&!",
        "AB&!AB|!|!",
    ]

    for case in cases:
        result = negation_normal_form(case)
        print(f"{case}: {result}")


if __name__ == "__main__":
    main()
