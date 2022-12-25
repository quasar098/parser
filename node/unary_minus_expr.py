import utils
from token import Token, TokenType


class UnaryMinusExpr:
    def __init__(self, expr=None):
        self.expr = expr

    def handle(self, token: Token):
        if self.expr is None:
            self.expr = utils.make_expr([token])
        raise NotImplementedError("unary minus already has expr")

    def __repr__(self):
        return f"<UnaryMinusExpr(expr={self.expr})>"

    def is_complete(self):
        return self.expr is not None
