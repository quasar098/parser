from typing import TextIO
from token import *


class Lexer:
    def __init__(self, file_object: TextIO):
        self.file = file_object

    def lex(self) -> list[Lexeme]:
        total: list[Lexeme] = []
        builder = ""
        char = None
        last_char = None
        in_string = False
        in_comment = False

        while True:
            last_char = char
            char = self.file.read(1)
            if char == "":
                if len(builder):
                    total.append(Lexeme(builder))
                break
            if in_string:
                if char == '"':
                    in_string = False
                    total.append(Lexeme(builder))
                    builder = ""
                    total.append(Lexeme('"'))
                    continue
                builder += char
                continue
            if in_comment:
                if char == "\n":
                    in_comment = False
                else:
                    print(char)
                    continue
            if last_char == "/" and char == "/":
                total = total[:-1]
                in_comment = True
                builder = ""
                continue
            if char in Lexeme.RESERVED:
                if char == '"':
                    in_string = True
                if len(builder):
                    total.append(Lexeme(builder))
                    builder = ""
                total.append(Lexeme(char))
                continue
            if builder in Lexeme.RESERVED:
                if char == " ":
                    total.append(Lexeme(builder))
                    builder = ""
                    continue
            if char == " ":
                if len(builder):
                    total.append(Lexeme(builder))
                    builder = ""
                continue
            builder += char

        return total

    @staticmethod
    def tokenize(lexemes: list[Lexeme]) -> list[Token]:
        total = []
        skip = 0
        for index, lexeme in enumerate(lexemes):
            if skip:
                skip -= 1
                continue
            if lexeme.is_reserved:
                if lexeme.content == '"':
                    total.append(Token(TokenType.STRING, lexemes[index+1].content))
                    skip = 2
                    continue
                total.append(Token(Lexeme.RESERVED[lexeme.content], lexeme.content))
            else:
                if lexeme.content[0].isnumeric():
                    total.append(Token(TokenType.INTEGER, lexeme.content))
                else:
                    total.append(Token(TokenType.IDENTIFIER, lexeme.content))
        return total

    def do(self):
        lexemes = self.lex()
        return Lexer.tokenize(lexemes)

    def __repr__(self):
        return f"<Lexer(file={self.file.name})>"
