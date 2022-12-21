from token import TokenType
from node.variable import Variable
from node.literalstringexpr import LiteralStringExpr


def from_token(token):
    if token.type == TokenType.VARIABLE:
        return Variable(token.content)
    if token.type == TokenType.STRING:
        return LiteralStringExpr(token.content)
    return token


def is_types(stuff, *types):
    from token import Token
    ctypes = [(type(thing) if isinstance(thing, Token) else thing) for thing in stuff]
    for index, t in enumerate(types):
        if len(ctypes) == index:
            return True
        if t == ctypes[index]:
            continue
        break
    else:
        return True
    return False
