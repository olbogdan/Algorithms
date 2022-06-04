# Give the root node of a tree, return an array where
# each element is the width of the tree at each level.
#   0
# 1  2  3
# 4     5
# answer: [1, 3, 2]
from collections import deque

from AlgoBootcamp.tree.Node import Node


def level_width(root):
    if root is None:
        return []
    counters = [0]
    queue = deque()
    queue.append(root)
    queue.append("level")

    while len(queue) > 1:
        node = queue.popleft()
        if node == "level":
            counters.append(0)
            queue.append("level")
        else:
            counters[-1] = counters[-1] + 1
            if node.children:
                queue.extend(node.children)
    return counters

node_level_0 = Node("0")
node_level_1_1 = Node("1.1")
node_level_1_2 = Node("1.2")
node_level_1_3 = Node("1.3")
node_level_2_1 = Node("2.1")
node_level_2_3 = Node("2.3")

node_level_0.children = [node_level_1_1, node_level_1_2, node_level_1_3]
node_level_1_1.children = [node_level_2_1]
node_level_1_3.children = [node_level_2_3]
node_level_2_3.children = [Node("3.3")]

print(level_width(node_level_0))



