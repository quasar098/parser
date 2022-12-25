import utils
from token import Token, TokenType
from node.identifier_expr import IdentifierExpr


class DeclareStatement:
    def __init__(self):
        self.identifier = IdentifierExpr()
        self.cache: list[Token] = []
        self.expr = None
        self.equals_found = False
        self.complete = False

    def __repr__(self):
        return f"<DeclareStatement(identifier={self.identifier}, expr={self.expr})>"

    def handle(self, token: Token):
        if not self.identifier.is_complete():
            if token.type != TokenType.IDENTIFIER:
                raise NotImplementedError("token type is not an identifier")
            self.identifier.name = token.content
            return
        if not self.equals_found:
            if token.type != TokenType.EQUALS:
                raise NotImplementedError("there is no equals")
            self.equals_found = True
            return
        if token.type == TokenType.NL:
            # todo handle expr
            self.expr = utils.make_expr(self.cache)
            self.cache = []
            self.complete = True
        else:
            self.cache.append(token)

    def is_complete(self):
        return self.complete and self.expr is not None and self.identifier is not None and self.equals_found

