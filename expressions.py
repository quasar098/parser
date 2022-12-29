from token import Token, TokenType


class SumExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def show(self):
        return {"left": self.left, "right": self.right}


class IdentifierExpr:
    def __init__(self, name=None):
        self.name: str = name

    def show(self):
        return {"name": self.name}


class IntegerExpr:
    def __init__(self, n=None):
        self.n: int = n

    def show(self):
        return {"num": self.n}


class StringExpr:
    def __init__(self, content=None):
        self.content: str = content

    def show(self):
        return {"content": self.content}
