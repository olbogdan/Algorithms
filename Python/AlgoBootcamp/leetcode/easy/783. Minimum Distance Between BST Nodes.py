# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105


from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = float(inf)

        def findMin(node, bottomVal, topVal):
            nonlocal result
            if not node:
                return
            if node.left:
                result = min(result, node.val - node.left.val)
                result = min(result, node.left.val - bottomVal)
                findMin(node.left, bottomVal, node.val)
            if node.right:
                result = min(result, topVal - node.right.val)
                result = min(result, node.right.val - node.val)
                findMin(node.right, node.val, topVal)

        findMin(root, float(-inf), float(inf))
        return int(result)


node = TreeNode(27, None, TreeNode(34, None, TreeNode(58, TreeNode(50, TreeNode(44, None, None)), None)))
sol = Solution()
res = sol.minDiffInBST(node)
assert res == 6

node = TreeNode(27, None, TreeNode(34, None, TreeNode(58, TreeNode(50, TreeNode(35, None, None)), None)))
res = sol.minDiffInBST(node)
assert res == 1
