from token_reader import TokenReader
from token import Token, TokenType


class DeclareStatement:
    def __init__(self, var=None, expr=None):
        self.variable = var
        self.expr = expr

    def __repr__(self):
        return f"<DeclareStatement(var={self.variable}, expr={self.expr})>"


class FuncCallStatement:
    def __init__(self, var=None, args=None):
        if args is None:
            args = []
        self.variable = var
        self.args = args

    def __repr__(self):
        return f"<FuncCallStatement(var={self.variable}, args={self.args})>"
