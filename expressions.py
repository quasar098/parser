from token import Token, TokenType


class SumExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def show(self):
        return {"left": self.left, "right": self.right}


class SubExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def show(self):
        return {"left": self.left, "right": self.right}


class MultiplyExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def show(self):
        return {"left": self.left, "right": self.right}


class DivideExpr:
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


class FuncCallExpr:
    def __init__(self, var=None, args=None):
        if args is None:
            args = []
        self.variable = var
        self.args = args

    def show(self):
        return {"var": self.variable, "args": self.args}


class IntegerExpr:
    def __init__(self, n=None):
        self.n: int = n

    def show(self):
        return {"num": self.n}


class UnaryMinusExpr:
    def __init__(self, n=None):
        self.n: int = n

    def show(self):
        return {"num": self.n}


class StringExpr:
    def __init__(self, content=None):
        self.content: str = content

    def show(self):
        return {"content": self.content}


class TrueExpr:
    def __init__(self):
        self.val = True


class FalseExpr:
    def __init__(self):
        self.val = False


class ComparisonEqualsExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def show(self):
        return {"left": self.left, "right": self.right}


class ComparisonOrExpr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def show(self):
        return {"left": self.left, "right": self.right}
