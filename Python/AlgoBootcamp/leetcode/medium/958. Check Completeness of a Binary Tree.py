# Given the root of a binary tree, determine if it is a complete binary tree.
#
# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# Example 2:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000


# Definition for a binary tree node.
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        gapFound = False
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                child = q.popleft()
                st1 = (child.left or child.right) and gapFound
                st2 = child.right and not child.left
                if st1 or st2:
                    return False
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
                if not child.right or (not child.right and not child.left):
                    gapFound = True
        return True


n = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6)))
sol = Solution()
res = sol.isCompleteTree(n)
print(res)
