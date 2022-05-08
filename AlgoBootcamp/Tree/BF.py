from collections import deque

from AlgoBootcamp.Tree.Node import Node


class Tree:
    def __init__(self):
        self.root: Node = None

    def traverse_bf(self, fn):
        if self.root is None:
            return
        nodes = deque()
        nodes.appendleft(self.root)
        while nodes:
            node = nodes.popleft()
            if node.children is not None:
                nodes.extend(node.children)
            fn(node.data)


tree = Tree()
assert tree.root is None


a = Node("A")
a1 = Node("A1")
a2 = Node("A2")
a22 = Node("A22")
a23 = Node("A23")
b = Node("B")
c = Node("C")
root = Node("Root")

root.children = [a, b, c]
a.children = [a1, a2]
a2.children = [a22]
a22.children = [a23]

tree = Tree()
tree.root = root

tree.traverse_bf(lambda node: print(node))