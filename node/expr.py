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
        from node.addexpr import AddExpr
        from node.subtractexpr import SubtractExpr
        from node.powerexpr import PowerExpr
        from node.literalintegerexpr import LiteralIntegerExpr

        if len(tokens) == 1:
            if isinstance(tokens[0], Expr):
                return tokens[0]
            return from_token(tokens[0])
        if is_types(tokens, LiteralIntegerExpr, TokenType.TIMES, TokenType.TIMES, LiteralIntegerExpr):
            base = Expr.from_tokens(tokens[:1])
            exponent = Expr.from_tokens(tokens[3:])
            return PowerExpr(base, exponent)
        if is_types(tokens, Variable, TokenType.LPAR):
            if tokens[-1].type == TokenType.RPAR:
                ivk_stmt = InvokeStatement(tokens[0])
                cache = []
                for token in tokens[2:-1]:
                    if isinstance(token, Token) and token.type == TokenType.COMMA:
                        ivk_stmt.args.append(Expr.from_tokens(cache))
                        cache.clear()
                        continue
                    cache.append(token)
                if len(cache):
                    ivk_stmt.args.append(Expr.from_tokens(cache))
                return ivk_stmt
            raise NotImplementedError(f"you are failure: {tokens}")
        if is_types(tokens, TokenType.ANYTHING, TokenType.PLUS, TokenType.ANYTHING):
            left = Expr.from_tokens(tokens[:1])
            right = Expr.from_tokens(tokens[2:])
            return AddExpr(left, right)
        if is_types(tokens, TokenType.ANYTHING, TokenType.MINUS, TokenType.ANYTHING):
            left = Expr.from_tokens(tokens[:1])
            right = Expr.from_tokens(tokens[2:])
            return SubtractExpr(left, right)
        if is_types(tokens, TokenType.LPAR):
            cache = []
            for token in tokens[1:]:
                if isinstance(token, Token) and token.type == TokenType.RPAR:
                    return Expr.from_tokens(cache)
                cache.append(token)
        raise NotImplementedError(f"not done yet: {tokens}")
