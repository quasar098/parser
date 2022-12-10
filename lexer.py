from typing import TextIO
from lexeme import Lexeme


class Lexer:
    def __init__(self, file_object: TextIO):
        self.file = file_object

    def lex(self) -> list[Lexeme]:
        total: list[Lexeme] = []
        builder = ""

        while True:
            char = self.file.read(1)
            if not char:
                if builder:
                    total.append(Lexeme(builder))
                break

            if char in Lexeme.RESERVED:
                if builder:
                    total.append(Lexeme(builder))
                    builder = ""
                total.append(Lexeme(char))
                continue
            if builder in Lexeme.RESERVED:
                if char == " ":
                    total.append(Lexeme(builder))
                    builder = ""
                    continue
            builder += char

        return total

    def __repr__(self):
        return f"<Lexer(file={self.file.name})>"
