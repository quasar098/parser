from node.block import Block
from node.node import Node


class Tree(Node):
    def __init__(self, tokens=()):
        super().__init__(tokens)
        self.block = Block()

    def __repr__(self):
        return f"<ParseTree(\n\tblock={self.block}\n)>"

    def handle(self, token):
        self.block.handle(token)

    def is_complete(self):
        return self.block.is_complete()
