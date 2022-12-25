from token import Token, TokenType


class StringLiteralExpr:
    def __init__(self, content=None):
        self.content = content

    def handle(self, token: Token):
        raise NotImplementedError("string literal cannot do handling")

    def __repr__(self):
        return f"<StringLiteralExpr(content={self.content})>"

    # noinspection PyMethodMayBeStatic
    def is_complete(self):
        return self.content is not None
