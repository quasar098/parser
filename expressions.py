from token import Token, TokenType


class SumExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<SumExpr(left={self.left}, right={self.right})>"


class IdentifierExpr:
    def __init__(self, name=None):
        self.name: str = name

    def __repr__(self):
        return f"<IdentifierExpr(name={self.name})>"


class IntegerExpr:
    def __init__(self, n=None):
        self.n: int = n

    def __repr__(self):
        return f"<IntegerExpr(n={self.n})>"


class StringExpr:
    def __init__(self, content=None):
        self.content: str = content

    def __repr__(self):
        return f"<StringExpr(content={self.content})>"
