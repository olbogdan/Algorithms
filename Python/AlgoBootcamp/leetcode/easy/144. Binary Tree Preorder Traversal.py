# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(node):
            if not node:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return result


sol = Solution()
node = TreeNode(1, TreeNode(2), TreeNode(3))
res = sol.preorderTraversal(node)
assert res[0] == 1
assert res[1] == 2
assert res[2] == 3


class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        result = []
        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            else:
                current = stack.pop()
        return result


sol = Solution2()
node = TreeNode(1, TreeNode(2), TreeNode(3))
res = sol.preorderTraversal(node)
assert res[0] == 1
assert res[1] == 2
assert res[2] == 3