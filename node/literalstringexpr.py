from node.expr import Expr


class LiteralStringExpr(Expr):
    def __init__(self, content: str = ""):
        super().__init__()
        self.content = content

    def __repr__(self):
        return f"<LiteralStringExpr(content={self.content})>"
