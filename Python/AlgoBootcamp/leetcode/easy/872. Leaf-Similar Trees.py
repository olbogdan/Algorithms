# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.fluttenTree(root1)
        leaves2 = self.fluttenTree(root2)

        return leaves1 == leaves2

    def fluttenTree(self, root):
        leaves = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves


node = TreeNode(10, TreeNode(9, TreeNode(1), TreeNode(2)), TreeNode(8, TreeNode(3), TreeNode(4)))
node2 = TreeNode(10, TreeNode(9, TreeNode(99), TreeNode(88)), TreeNode(8, TreeNode(77), TreeNode(66)))
sol = Solution()
res = sol.leafSimilar(node, node2)
assert res is False
res = sol.leafSimilar(node, node)
assert res is True


class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        interrupt = False

        def interruptFun():
            nonlocal interrupt
            return interrupt

        leaves = []
        self.iterateLeaves(root1, lambda x: leaves.append(x), interruptFun)

        i = 0

        def compareLevels(x):
            nonlocal i
            nonlocal leaves
            nonlocal interrupt
            if i >= len(leaves) or leaves[i] != x:
                interrupt = True
                return
            i += 1

        self.iterateLeaves(root2, compareLevels, interruptFun)

        return not interrupt and i == len(leaves)

    def iterateLeaves(self, root, callable, interrupt):
        stack = []
        stack.append(root)
        while stack:
            if interrupt():
                break
            node = stack.pop()
            if not node.left and not node.right:
                callable(node.val)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

