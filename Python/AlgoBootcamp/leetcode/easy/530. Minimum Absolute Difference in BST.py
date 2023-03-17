# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
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
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105
# #DFS #inordertraversal
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float(inf)
        prev = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            nonlocal result
            nonlocal prev
            # Attention: if prev is 0 it would consider as false, Check on None is required
            if prev is not None:
                result = min(result, node.val - prev)
            prev = node.val

            dfs(node.right)

        dfs(root)
        return result


node = TreeNode(27, None, TreeNode(34, None, TreeNode(58, TreeNode(50, TreeNode(44, None, None)), None)))
sol = Solution()
res = sol.getMinimumDifference(node)
assert res == 6

node = TreeNode(27, None, TreeNode(34, None, TreeNode(58, TreeNode(50, TreeNode(35, None, None)), None)))
res = sol.getMinimumDifference(node)
assert res == 1

node = TreeNode(1, None, TreeNode(2236, TreeNode(519), TreeNode(2776)))
res = sol.getMinimumDifference(node)
print(res)
assert res == 519
