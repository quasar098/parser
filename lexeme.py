class Lexeme:
    RESERVED = [
        "if",
        "print",
        "(",
        ")",
        "+",
        "*",
        "-",
        "/",
        "%",
        '"',
        "\n"
    ]

    def __init__(self, content: str):
        self.content = content

    def __repr__(self):
        bsn = '\n'
        bsn_ = "\\n"
        return f"<Lexeme({self.content if self.content is not bsn else bsn_})>"
