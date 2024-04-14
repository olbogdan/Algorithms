# Given the root of a binary tree, return the sum of all left leaves.
#
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:
#
# Input: root = [1]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        if root.left and not root.left.left and not root.left.right:
            result = root.left.val
        result += self.sumOfLeftLeaves(root.left)
        result += self.sumOfLeftLeaves(root.right)
        return result


sol = Solution()
node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
assert sol.sumOfLeftLeaves(node1) == 24
node1 = TreeNode(1)
assert sol.sumOfLeftLeaves(node1) == 0
