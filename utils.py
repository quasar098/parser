from token import TokenType, Token
from node.variable import Variable
from node.literalstringexpr import LiteralStringExpr
from node.literalintegerexpr import LiteralIntegerExpr


def from_token(token):
    if not isinstance(token, Token):
        return token
    if token.type == TokenType.VARIABLE:
        return Variable(token.content)
    if token.type == TokenType.STRING:
        return LiteralStringExpr(token.content)
    if token.type == TokenType.INTEGER:
        return LiteralIntegerExpr(int(token.content))
    return token


def is_types(stuff, *types):
    from token import Token
    ctypes = [(type(thing) if not isinstance(thing, Token) else thing.type) for thing in stuff]
    for index, t in enumerate(types):
        if len(ctypes) == index:
            return True
        if t == TokenType.ANYTHING:
            continue
        if t != ctypes[index]:
            return False
    return True
