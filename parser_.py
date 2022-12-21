from tree import Tree
import node.node as node
from token import Token, TokenType


class Parser:
    @staticmethod
    def do(tokens):
        tree = Tree()

        # remove trailing NLs
        while len(tokens) and tokens[-1].type == TokenType.NL:
            tokens = tokens[:-1]

        last_was_nl = True
        for token in tokens:
            if last_was_nl:
                if token.type == TokenType.NL:
                    continue
                else:
                    last_was_nl = False
            if token.type == TokenType.NL:
                last_was_nl = True
            tree.handle(token)
        tree.handle(Token(TokenType.NL, "\n"))
        return tree
