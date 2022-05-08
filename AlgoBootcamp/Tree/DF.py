from collections import deque

from AlgoBootcamp.Tree.Node import Node


class Tree:
    def __init__(self):
        self.root: Node = None

    def traverse_df(self, fn):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node.children is not None:
                for i in reversed(node.children):
                    queue.appendleft(i)
                # for i in range(1, len(node.children)+1):
                #     queue.appendleft(node.children[-i])
            fn(node)


tree = Tree()
assert tree.root is None


a = Node("A")
a1 = Node("A1")
a2 = Node("A2")
a22 = Node("A2_2")
a223 = Node("A2_2_3")
b = Node("B")
c = Node("C")
root = Node("Root")

root.children = [a, b, c]
a.children = [a1, a2]
a2.children = [a22]
a22.children = [a223]

tree = Tree()
tree.root = root

tree.traverse_df(lambda node: print(node))