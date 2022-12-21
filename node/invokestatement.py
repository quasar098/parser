from node.statement import Statement


class InvokeStatement(Statement):
    def __init__(self, name=""):
        from node.expr import Expr
        super().__init__()
        self.name = name
        self.args: list[Expr] = []

    def __repr__(self):
        return f"<InvokeStatement(name={self.name}, args={self.args})>"

    def handle(self, token):
        pass
