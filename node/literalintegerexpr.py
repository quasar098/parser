from node.expr import Expr


class LiteralIntegerExpr(Expr):
    def __init__(self, n: int = 0):
        super().__init__()
        self.n = n

    def __repr__(self):
        return f"<LiteralIntegerExpr(n={self.n})>"
