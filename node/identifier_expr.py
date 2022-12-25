from token import Token, TokenType


class IdentifierExpr:
    def __init__(self):
        self.name = None

    def __repr__(self):
        return f"<IdentifierExpr(name={self.name})>"

    def handle(self, token: Token):
        if self.name is not None:
            raise NotImplementedError(f"the name is not none, it is {self.name}")
        if token.type == TokenType.IDENTIFIER:
            self.name = token.content

    def is_complete(self):
        return self.name is not None
