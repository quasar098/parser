

class Block:
    def __init__(self):
        self.statements = []

    def __repr__(self):
        return f"<Block(statements={self.statements})>"
