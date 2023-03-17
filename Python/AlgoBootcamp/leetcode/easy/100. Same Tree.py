# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Input: p = [1,2], q = [1,null,2]
# Output: false
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p and q or p and not q:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False


l1 = TreeNode(1)
r1 = TreeNode(2)
p = TreeNode(3, l1, r1)
q = TreeNode(3, l1, r1)
assert isSameTree(p, q) == True
q = TreeNode(3, r1, l1)
assert isSameTree(p, q) == False