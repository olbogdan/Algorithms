# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    left = root.left
    right = root.right
    root.right = left
    root.left = right
    invertTree(left)
    invertTree(right)
    return root

tr1 = TreeNode(11, None, None)
tr2 = TreeNode(12, None, None)
TreeNode(12, tr1, tr2)
result = invertTree(TreeNode(12, tr1, tr2))
assert result.left.val == 12