# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
#
# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
#
#
#
# Example 1:
#
#
#
# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
# Example 2:
#
#
#
# Input: root = [1,3,3,3,2], target = 3
# Output: [1,3,null,null,2]
# Example 3:
#
#
#
# Input: root = [1,2,null,2,null,2], target = 2
# Output: [1]
# Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 3000].
# 1 <= Node.val, target <= 1000
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteLeaf(node):
            if node.left:
                node.left = deleteLeaf(node.left)
            if node.right:
                node.right = deleteLeaf(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            else:
                return node

        return deleteLeaf(root)


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
newRoot = sol.removeLeafNodes(root, 2)
assert newRoot.val == 1
assert newRoot.right.val == 3
assert newRoot.right.right.val == 4
assert not newRoot.left
assert not newRoot.right.left
