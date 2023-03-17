# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values
# of the nodes you can see ordered from top to bottom.
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:
#
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
#
# Input: root = []
# Output: []
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    deq = deque()
    deq.append(root)
    while deq:
        for i in range(len(deq)):
            node = deq.pop()
            if i == 0:
                result.append(node.val)
            if node.right: deq.appendleft(node.right)
            if node.left: deq.appendleft(node.left)
    return result


assert rightSideView(None) == []

node = TreeNode(1)
assert rightSideView(node) == [1]

node = TreeNode(1, TreeNode(2), TreeNode(3))
assert rightSideView(node) == [1, 3]

node = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
assert rightSideView(node) == [1, 3, 4]