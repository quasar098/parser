from node.block import Block


class Tree:
    def __init__(self):
        super().__init__()
        self.block = Block()

    def __repr__(self):
        return f"<ParseTree(block={self.block})>"

    def handle(self, token):
        self.block.handle(token)

    def is_complete(self):
        return self.block.is_complete()
