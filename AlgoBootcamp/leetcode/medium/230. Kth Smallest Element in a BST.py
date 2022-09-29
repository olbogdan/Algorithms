# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    array = []
    def dfs(root):
        if root.left:
            dfs(root.left)
        array.append(root.val)
        if root.right:
            dfs(root.right)
    dfs(root)
    return array[k - 1]


assert kthSmallest(TreeNode(2, TreeNode(1), TreeNode(3)), 1) == 1
assert kthSmallest(TreeNode(2, TreeNode(1), TreeNode(3)), 2) == 2
assert kthSmallest(TreeNode(2, TreeNode(1), TreeNode(3)), 3) == 3


def kthSmallest2(root: Optional[TreeNode], k: int) -> int:
    res = 0
    def dfs(root):
        nonlocal k
        nonlocal res
        if not root or k == 0:
            return
        dfs(root.left)
        k -= 1
        if k == 0:
            res = root.val
        dfs(root.right)
    dfs(root)
    return res


assert kthSmallest2(TreeNode(2, TreeNode(1), TreeNode(3)), 1) == 1
assert kthSmallest2(TreeNode(2, TreeNode(1), TreeNode(3)), 2) == 2
assert kthSmallest2(TreeNode(2, TreeNode(1), TreeNode(3)), 3) == 3