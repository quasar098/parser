from token import TokenType, Token


class Node:
    def __init__(self, nodes=()):
        self.nodes: list["Node"] = list(nodes)
        self.cache = []

    def handle(self, token):
        pass

    def is_complete(self):
        pass

    def get_cache_types(self):
        return [(type(w2) if not isinstance(w2, Token) else w2.type) for w2 in self.cache]

    def is_cache_types(self, *types):
        ctypes = self.get_cache_types()
        for index, t in enumerate(types):
            if len(ctypes) == index:
                return True
            if t == ctypes[index]:
                continue
            break
        else:
            return True
        return False

    # the way that this works is that there is a tree structure with nodes connecting to nodes and when a token gets
    # handled by the top of the tree, the top sends it down a level etc. a certain node down the chain will decide that
    # it is a good idea to add the node to its list of nodes instead of sending the node down the rest of the chain

    # an example of this would be if the tree > block of code decides to create a new top level node
    # if the nodes "var","pasta","=","3" have already been handled by the *tree > *block > *statement,
    # the block can create a new statement alongside the *tree > *block > statement *statement
    # that way, the second statement will start being edited
