from tree import Tree
import node.node as node
from token import Token, TokenType


class Parser:
    @staticmethod
    def do(tokens):
        tree = Tree()
        for token in tokens:
            tree.handle(token)
        tree.handle(Token(TokenType.NL, "\n"))
        return tree
