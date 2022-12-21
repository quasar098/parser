from node.expr import Expr
from typing import Optional


class AddExpr(Expr):
    def __init__(self, left=None, right=None):
        super().__init__()
        self.left: Optional[Expr] = left
        self.right: Optional[Expr] = right

    def __repr__(self):
        return f"<AddExpr(left={self.left}, right={self.right})>"
