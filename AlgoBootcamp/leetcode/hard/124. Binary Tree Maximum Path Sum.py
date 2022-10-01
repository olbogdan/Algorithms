# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    result = float(-inf)

    def dfs(root):
        nonlocal result
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        currRootNodeMax = max(root.val + left, root.val + right, root.val + left + right, root.val)
        result = max(result, currRootNodeMax)
        return max(root.val + left, root.val + right, root.val)
    dfs(root)
    return result


node = TreeNode(1, TreeNode(2), TreeNode(3))
assert maxPathSum(node) == 6