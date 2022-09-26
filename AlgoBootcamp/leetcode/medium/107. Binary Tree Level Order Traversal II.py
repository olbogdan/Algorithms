# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
# (i.e., from left to right, level by level from leaf to root).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    stack = deque()
    stack.append(root)
    result = deque()
    while stack:
        level = []
        for i in range(len(stack)):
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            level.append(node.val)
        result.appendleft(level)
    return list(result)


node = TreeNode(10, TreeNode(20), TreeNode(30, TreeNode(40), TreeNode(60)))
assert levelOrderBottom(node) == [[40, 60], [20, 30], [10]]