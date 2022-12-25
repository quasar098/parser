from token import Token, TokenType
from node.declare_statement import DeclareStatement


class Block:
    def __init__(self):
        self.statements = []

    def __repr__(self):
        return f"<Block(statements={self.statements})>"

    def handle(self, token: Token):
        if self.is_complete():
            if token.type == TokenType.DECL:
                self.statements.append(DeclareStatement())
            return
        self.statements[-1].handle(token)

    def is_complete(self):
        return all([statement.is_complete() for statement in self.statements])
