# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
#
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
# Example 2:
#
#
# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -1000 <= Node.val <= 1000
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        arr = []
        def dfs(node):
            if not node:
                return
            arr.append(str(node.val))
            # append a brace for left if any child exist
            if node.left or node.right:
                arr.append("(")
            dfs(node.left)
            if node.left or node.right:
                arr.append(")")
            # append a brace for right only if it is exist
            if node.right:
                arr.append("(")
                dfs(node.right)
                arr.append(")")

        dfs(root)
        return "".join(arr)


sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
res = sol.tree2str(root)
assert res == "1(2)(3)"
root = TreeNode(1, None, TreeNode(3, None, TreeNode(4)))
res = sol.tree2str(root)
assert res == "1()(3()(4))"
