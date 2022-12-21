from node.expr import Expr
from typing import Optional


class PowerExpr(Expr):
    def __init__(self, base=None, exponent=None):
        super().__init__()
        self.base: Optional[Expr] = base
        self.exponent: Optional[Expr] = exponent

    def __repr__(self):
        return f"<PowerExpr(base={self.base}, exponent={self.exponent})>"
