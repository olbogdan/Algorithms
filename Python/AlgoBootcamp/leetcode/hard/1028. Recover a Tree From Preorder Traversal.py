# We run a preorder depth-first search (DFS) on the root of a binary tree.
#
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
#
# If a node has only one child, that child is guaranteed to be the left child.
#
# Given the output traversal of this traversal, recover the tree and return its root.
#
#
#
# Example 1:
#
#
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# Example 2:
#
#
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# Example 3:
#
#
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
#
#
# Constraints:
#
# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 109
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levelToNodes = deque()  # (level, value)
        i = 0
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            number = 0
            while i < len(traversal) and traversal[i] != '-':
                number *= 10
                number += int(traversal[i])
                i += 1
            levelToNodes.append((level, number))

        def dfs(level, parent):
            if not parent:
                return
            while len(levelToNodes) > 0 and levelToNodes[0][0] == level:
                _, value = levelToNodes.popleft()
                if parent.left is None:
                    parent.left = TreeNode(value)
                    dfs(level + 1, parent.left)
                else:
                    parent.right = TreeNode(value)
                    dfs(level + 1, parent.right)

        dummyNode = TreeNode()
        dfs(0, dummyNode)
        return dummyNode.left


sol = Solution()
assert sol.recoverFromPreorder("1-2--3--4-5--6--7").val == 1
assert sol.recoverFromPreorder("1-2--3--4-5--6--7").left.val == 2
assert sol.recoverFromPreorder("1-2--3--4-5--6--7").right.val == 5
assert sol.recoverFromPreorder("1-2--3--4-5--6--7").right.left.val == 6
assert sol.recoverFromPreorder("1-2--3--4-5--6--7").right.right.val == 7
assert  sol.recoverFromPreorder("1-2--3--4-5--6--7").left.left.val == 3
assert sol.recoverFromPreorder("1-2--3--4-5--6--7").left.right.val == 4