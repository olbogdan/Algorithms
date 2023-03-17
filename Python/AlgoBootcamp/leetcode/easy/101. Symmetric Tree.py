# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
# Follow up: Could you solve it both recursively and iteratively?
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root.left, root.right))
        while q:
            size = len(q)
            for _ in range(size):
                L, R = q.popleft()
                if not L and not R:
                    continue
                elif not L or not R or L.val != R.val:
                    return False
                q.append((L.right, R.left))
                q.append((L.left, R.right))
        return True


sol = Solution()
n = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
res = sol.isSymmetric(n)
assert res is True


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2 or n1.val != n2.val:
                return False
            return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
        return isMirror(root.left, root.right)


sol = Solution2()
n = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
res = sol.isSymmetric(n)
assert res is True
