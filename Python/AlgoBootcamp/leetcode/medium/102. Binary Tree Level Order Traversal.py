# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
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


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []

    stack = deque()
    stack.append(root)
    while stack:
        level = []
        for i in range(len(stack)):
            node = stack.pop()
            level.append(node.val)
            if node.left:
                stack.appendleft(node.left)
            if node.right:
                stack.appendleft(node.right)
        result.append(level)
    return result


node = TreeNode(10, TreeNode(1), TreeNode(100, TreeNode(3), TreeNode(500)))
assert levelOrder(node) == [[10], [1, 100], [3, 500]]