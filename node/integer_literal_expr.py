from token import Token, TokenType


class IntegerLiteralExpr:
    def __init__(self, number=None):
        self.number = number

    def __repr__(self):
        return f"<IntegerLiteralExpr(number={self.number})>"

    def handle(self, token: Token):
        raise NotImplementedError("integer literal cannot handle tokens")

    def is_complete(self):
        return self.number is not None
