# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest. You may return the result in any order.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:
#
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
#
#
# Constraints:
#
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        res = []

        def dfs(node, parent):
            nonlocal delete
            nonlocal res
            if not node:
                return

            if node.val in delete:
                dfs(node.left, None)
                dfs(node.right, None)
            else:
                dfs(node.left, node)
                dfs(node.right, node)
                if parent is None:
                    res.append(node)

            if node.left and node.left.val in delete:
                node.left = None
            if node.right and node.right.val in delete:
                node.right = None

        dfs(root, None)
        return res


sol = Solution()
nodes = sol.delNodes(TreeNode(1, TreeNode(2), TreeNode(3)), [1])
assert len(nodes) == 2
assert nodes[0].val == 2
assert nodes[1].val == 3