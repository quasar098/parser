from node.node import Node
from node.variable import Variable
from utils import from_token
from token import TokenType, Token
from node.declarestatement import DeclareStatement
from node.expr import Expr


class Block(Node):
    def __init__(self, nodes=()):
        super().__init__(nodes)

    def __repr__(self):
        return f"<Block(statements={self.nodes})>"

    # noinspection PyTypeChecker
    def handle(self, token):
        # declare variable
        if self.is_cache_types(TokenType.DECL, Variable, TokenType.EQUALS):
            if token.type == TokenType.NL:
                self.nodes.append(DeclareStatement(self.cache[1].name, Expr.from_tokens(self.cache[3:])))
                self.cache.clear()
                return
        if self.is_cache_types(Variable, TokenType.LPAR):
            if token.type == TokenType.NL:
                invoke_expr = Expr.from_tokens(self.cache)
                self.nodes.append(invoke_expr)
                self.cache.clear()
                return
        if not len(self.cache) or isinstance(token, Token) or self.cache[len(self.cache)-1].is_complete():
            self.cache.append(from_token(token))

    def is_complete(self):
        return [node.is_complete() for node in self.nodes]
