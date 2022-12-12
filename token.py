from enum import Enum


class TokenType(Enum):
    IF = 100
    PRINT = 101
    LPAR = 102
    RPAR = 103
    LCURLY = 104
    RCURLY = 105
    COLON = 106
    PLUS = 107
    TIMES = 108
    MINUS = 109
    SLASH = 110
    MODULO = 111
    QUOTE = 112
    EQUALS = 113
    PERIOD = 114
    VAR = 115
    NL = 116

    VARIABLE = 1
    STRING = 2
    NUMBER = 3
    FLOAT = 4


class Lexeme:
    RESERVED = {
        "if": TokenType.IF,
        "print": TokenType.PRINT,
        "(": TokenType.LPAR,
        ")": TokenType.RPAR,
        "{": TokenType.LCURLY,
        "}": TokenType.RCURLY,
        ":": TokenType.COLON,
        "+": TokenType.PLUS,
        "*": TokenType.TIMES,
        "-": TokenType.MINUS,
        "/": TokenType.SLASH,
        "%": TokenType.MODULO,
        '"': TokenType.QUOTE,
        "=": TokenType.EQUALS,
        ".": TokenType.PERIOD,
        "var": TokenType.VAR,
        "\n": TokenType.NL
    }

    def __init__(self, content: str):
        self.content = content

    @property
    def is_reserved(self):
        return self.content in Lexeme.RESERVED

    def __repr__(self):
        bsn = '\n'
        bsn_ = "\\n"
        return f"<Lexeme({self.content if self.content is not bsn else bsn_})>"


class Token:
    def __init__(self, token_type: TokenType, content: str):
        self.type = token_type
        self.content = content

    def __repr__(self):
        bsn = "\n"
        bsn_ = "\\n"
        return f"<Token(type={self.type}, content={'{'}{self.content if self.content != bsn else bsn_}{'}'})>"
