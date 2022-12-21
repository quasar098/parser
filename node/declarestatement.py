from node.statement import Statement


class DeclareStatement(Statement):
    def __init__(self, name=None, expr=None):
        super().__init__()
        self.name = name
        self.expr = expr

    def __repr__(self):
        return f"<DeclareStatement(name={self.name}, expr={self.expr})>"

    def handle(self, token):
        raise NotImplementedError("this should not happen")

    def is_complete(self):
        return self.name is not None and self.expr is not None
