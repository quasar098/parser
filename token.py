from enum import Enum


class TokenType(Enum):
    IF = 100
    ELSE = 101
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
    PIPE = 115
    NL = 116
    COMMA = 117
    FUNC = 118
    LANGLE = 119
    RANGLE = 120

    IDENTIFIER = 1
    STRING = 2
    INTEGER = 3
    FLOAT = 4
    FALSE = 5
    TRUE = 6


class Lexeme:
    RESERVED = {
        "if": TokenType.IF,
        "else": TokenType.ELSE,
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
        "\n": TokenType.NL,
        ",": TokenType.COMMA,
        "func": TokenType.FUNC,
        "false": TokenType.FALSE,
        "true": TokenType.TRUE,
        "|": TokenType.PIPE,
        ">": TokenType.RANGLE,
        "<": TokenType.LANGLE
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


class NoToken:
    def __init__(self):
        self.type = None
        self.content = None

    def __bool__(self):
        return False


class Token:
    def __init__(self, token_type: TokenType, content: str):
        self.type = token_type
        self.content = content

    def __repr__(self):
        bsn = "\n"
        bsn_ = "\\n"
        return f"<Token(type={self.type}, content={'{'}{self.content if self.content != bsn else bsn_}{'}'})>"
