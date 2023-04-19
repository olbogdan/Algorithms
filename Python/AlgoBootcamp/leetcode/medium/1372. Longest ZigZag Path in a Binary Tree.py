# You are given the root of a binary tree.
#
# A ZigZag path for a binary tree is defined as follow:
#
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
#
# Return the longest ZigZag path contained in that tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:
#
#
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:
#
# Input: root = [1]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 5 * 104].
# 1 <= Node.val <= 100

from enum import Enum
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        result = 0

        def dfs(node, direction):
            nonlocal result
            if not node:
                return 0
            notZigZag = 0
            zigZag = 0
            if direction == Direction.RIGHT:
                notZigZag = dfs(node.right, Direction.RIGHT)
                zigZag = 1 + dfs(node.left, Direction.LEFT)
            else:
                notZigZag = dfs(node.left, Direction.LEFT)
                zigZag = 1 + dfs(node.right, Direction.RIGHT)
            result = max(result, zigZag, notZigZag)
            return zigZag

        dfs(root.right, Direction.RIGHT)
        dfs(root.left, Direction.LEFT)
        return result

sol = Solution()
assert sol.longestZigZag(TreeNode(left=TreeNode(right=TreeNode()))) == 2
