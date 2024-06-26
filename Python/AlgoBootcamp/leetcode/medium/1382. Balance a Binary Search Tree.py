# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
#
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,1,3]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArr = []

        def inorderTraverse(root: TreeNode) -> None:
            if not root:
                return
            inorderTraverse(root.left)
            sortedArr.append(root)
            inorderTraverse(root.right)

        def sortedArrayToBST(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = (start + end) // 2
            root = sortedArr[mid]
            root.left = sortedArrayToBST(start, mid - 1)
            root.right = sortedArrayToBST(mid + 1, end)
            return root

        inorderTraverse(root)
        return sortedArrayToBST(0, len(sortedArr) - 1)


sol = Solution()
assert sol.balanceBST(TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))) is not None
assert sol.balanceBST(TreeNode(2, TreeNode(1), TreeNode(3))) is not None
assert sol.balanceBST(TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))) is not None
