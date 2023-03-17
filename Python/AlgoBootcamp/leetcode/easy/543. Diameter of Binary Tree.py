# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
#
# Input: root = [1,2]
# Output: 1
from typing import Optional


class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    result = 0

    def dfs(node):
        nonlocal result
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)


        # possible maximum sub root node if it's chils (left + right) bigger then the root
        result = max(result, left + right)

        # return bigger of left or right + 1
        if left > right:
            return left + 1
        else:
            return right + 1

    dfs(root)
    return result


node = TreeNode(10, TreeNode(20), TreeNode(30, TreeNode(40), TreeNode(60)))
assert diameterOfBinaryTree(node) == 3