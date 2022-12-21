from node.node import Node
from token import Token, TokenType


class Expr(Node):
    def __init__(self):
        super().__init__()

    # noinspection PyTypeChecker
    @staticmethod
    def from_tokens(tokens: list[Token]) -> "Expr":
        from utils import from_token
        from node.variable import Variable
        from node.invokestatement import InvokeStatement
        from utils import is_types

        if len(tokens) == 1:
            if isinstance(tokens[0], Expr):
                return tokens[0]
            return from_token(tokens[0])
        if is_types(tokens, Variable, TokenType.LPAR):
            if isinstance(tokens[-1], TokenType.RPAR):
                ivk_stmt = InvokeStatement(tokens[0])
                cache = []
                for token in tokens[2:-1]:
                    if token.type == TokenType.COMMA:
                        ivk_stmt.args.append(Expr.from_tokens(cache))
                        cache.clear()
                        continue
                    cache.append(token)
                if len(cache):
                    ivk_stmt.args.append(Expr.from_tokens(cache))
                return ivk_stmt
            raise NotImplementedError(f"you are failure: {tokens}")
        raise NotImplementedError(f"not done yet: {tokens}")
