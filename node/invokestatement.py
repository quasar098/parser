from node.statement import Statement


class InvokeStatement(Statement):
    def __init__(self, name=""):
        from expr import Expr
        super().__init__()
        self.name = name
        self.args: list[Expr] = []

    def handle(self, token):
        pass
