from token_reader import TokenReader
from token import Token, TokenType


class DeclareStatement:
    def __init__(self, var=None, expr=None):
        self.variable = var
        self.expr = expr

    def show(self):
        return {"var": self.variable, "expr": self.expr}


class DeclareFunctionStatement:
    def __init__(self, var=None, expr=None):
        self.variable = var
        self.block = expr

    def show(self):
        return {"var": self.variable, "block": self.block}


class FuncCallStatement:
    def __init__(self, expr=None):
        self.expr = expr

    def show(self):
        return {"expr": self.expr}


class IfStatement:
    def __init__(self, cond=None, block=None):
        self.condition = cond
        self.block = block

    def show(self):
        return {"condition": self.condition, "block": self.block}
