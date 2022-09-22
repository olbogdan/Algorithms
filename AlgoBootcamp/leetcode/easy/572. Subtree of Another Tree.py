# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
from collections import deque
from typing import Optional


# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isEquals(tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif not tree1 or not tree2:
            return False
        return tree1.val == tree2.val and isEquals(tree1.left, tree2.left) and isEquals(tree1.right, tree2.right)

    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            item = queue.pop()
            if item:
                queue.appendleft(item.left)
                queue.appendleft(item.right)
                if isEquals(item, subRoot):
                    return True
    return False

l1 = TreeNode(1)
r1 = TreeNode(2)
p = TreeNode(3, l1, r1)
q = TreeNode(3, l1, r1)
assert isSubtree(p, q) == True

l1 = TreeNode(1)
r1 = TreeNode(2)
p = TreeNode(3, l1, r1)
p2level = TreeNode(10, None, p)
q = TreeNode(3, l1, r1)
assert isSubtree(p2level, q) == True

l1 = TreeNode(1)
p = TreeNode(3, l1, None)
assert isSubtree(p, l1) == True

l1 = TreeNode(1, TreeNode(3))
r1 = TreeNode(1)
p = TreeNode(3, l1, None)
assert isSubtree(p, r1) == False