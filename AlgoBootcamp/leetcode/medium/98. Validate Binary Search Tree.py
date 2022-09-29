from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def isValid(root, bottomBorder, topBorder):
        if root.val <= bottomBorder or root.val >= topBorder:
            return False
        leftValid = True
        if root.left:
            leftValid = isValid(root.left, bottomBorder, root.val)
        rightValid = True
        if root.right:
            rightValid = isValid(root.right, root.val, topBorder)
        return leftValid and rightValid

    return isValid(root, float(-inf), float(inf))


print(isValidBST(TreeNode(2, TreeNode(2), TreeNode(2))))