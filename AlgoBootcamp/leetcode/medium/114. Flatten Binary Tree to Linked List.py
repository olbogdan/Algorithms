# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
#
#
# Example 1:
#
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            # while left size exist, move it right
            # find the right most point in the left subtree
            # old right should be attached to rights item of left
            if cur.left:
                rightMostOfLeft = cur.left
                while rightMostOfLeft.right:
                    rightMostOfLeft = rightMostOfLeft.right

                rightMostOfLeft.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right


t = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
sol.flatten(t)
assert t.val == 1
assert t.right.val == 2
assert t.right.right.val == 3
