from token import TokenType, Token


def make_expr(tokens: list[Token]):
    import node
    if len(tokens) == 0:
        raise NotImplementedError("len tokens is 0")

    # string literal
    if len(tokens) == 1 and tokens[0].type == TokenType.STRING:
        return node.string_literal_expr.StringLiteralExpr(tokens[0].content)

    # unary minus
    if len(tokens) == 2 and tokens[0].type == TokenType.MINUS and tokens[1].type == TokenType.INTEGER:
        return node.unary_minus_expr.UnaryMinusExpr(make_expr(tokens[1:]))

    # integer literal
    if len(tokens) == 1 and tokens[0].type == TokenType.INTEGER:
        return node.integer_literal_expr.IntegerLiteralExpr(int(tokens[0].content))

    raise NotImplementedError(f"can't find rule: {tokens}")
