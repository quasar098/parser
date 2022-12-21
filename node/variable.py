from node.node import Node


class Variable(Node):
    def __init__(self, name=None, nodes=()):
        self.name = name
        super().__init__(nodes)

    def handle(self, token):
        raise NotImplementedError("this variable node is leaflet, not branch")

    def __repr__(self):
        return f"<Variable(name={self.name})>"

    def is_complete(self):
        return self.name is not None
