# Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
#
# Note that the root node is at depth 1.
#
# The adding rule is:
#
# Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
# cur's original left subtree should be the left subtree of the new left subtree root.
# cur's original right subtree should be the right subtree of the new right subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
#
#
# Example 1:
#
#
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]
# Example 2:
#
#
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# The depth of the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# -105 <= val <= 105
# 1 <= depth <= the depth of tree + 1
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        def dfs(node, level):
            if not node:
                return
            if level == 1:
                nLeft = node.left
                nRight = node.right
                nNodeLeft = TreeNode(val, nLeft)
                nNodeRight = TreeNode(val, nRight)
                node.left = nNodeLeft
                node.right = nNodeRight
                return
            else:
                dfs(node.left, level - 1)
                dfs(node.right, level - 1)

        dfs(root, depth - 1)
        return root


sol = Solution()
node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(6)
node4 = TreeNode(3)
node5 = TreeNode(1)
node6 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node = sol.addOneRow(node1, 1, 2)
assert node.val == 4
assert node.left.val == 1
assert node.right.val == 1
assert node.left.left.val == 2
assert node.left.right is None

