# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#
# Input: root = []
# Output: true

from collections import deque
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
   result = True
   def dfs(node):
       if not node:
           return 0
       nonlocal result
       left = dfs(node.left)
       right = dfs(node.right)
       if left > right and left - right > 1:
           result = False
       elif left < right and right - left > 1:
           result = False
       return max(left, right) + 1
   dfs(root)
   return result


node = TreeNode(10, TreeNode(2), TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)))
assert isBalanced(node) == False

node = TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3)))
assert isBalanced(node) == True


def isBalanced2(root: Optional[TreeNode]) -> bool:
    # find the smallest node without chils, it will be min height
    # find the deepest tree level
    # deep - min <= 1 is ture result
    if not root:
        return True
    minLevel = float(inf)
    maxLevel = 0

    stack = deque()
    stack.append([root, 0])
    while stack:
        # level up
        for i in range(len(stack)):
            node, level = stack.popleft()
            maxLevel = max(maxLevel, level)
            if not node.left and not node.right:
                # some lonely node is found
                minLevel = min(minLevel, level)

            level += 1
            if node.left:
                stack.append([node.left, level])
            if node.right:
                stack.append([node.right, level])
    return maxLevel - minLevel <= 1


node = TreeNode(10, TreeNode(2), TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)))
assert isBalanced2(node) == False