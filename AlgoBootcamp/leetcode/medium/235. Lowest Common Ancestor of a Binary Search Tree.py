# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
# Example:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#
# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


tr1 = TreeNode(1)
tr4 = TreeNode(4)
tree = TreeNode(5, TreeNode(3, tr1, tr4))
assert lowestCommonAncestor(tree, TreeNode(1), TreeNode(4)).val == 3