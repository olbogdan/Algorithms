# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.
#
#
#
# Example 1:
#
#
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
# Example 2:
#
#
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 2 <= n <= 105
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def dfs(node, target, direction):
            if not node:
                return None

            if node.val == target:
                return [(node.val, direction)]

            leftPath = dfs(node.left, target, "L")
            if leftPath:
                leftPath.append((node.val, direction))
                return leftPath

            rightPath = dfs(node.right, target, "R")
            if rightPath:
                rightPath.append((node.val, direction))
                return rightPath

            return None

        startPath = dfs(root, startValue, None)
        destPath = dfs(root, destValue, None)
        while len(startPath) > 0 and len(destPath) > 0 and startPath[-1][0] == destPath[-1][0]:
            startPath.pop()
            destPath.pop()

        resArr = ["U"] * len(startPath)

        destPath.reverse()
        for val, direction in destPath:
            resArr.append(direction)
        return "".join(resArr)


sol = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)
assert sol.getDirections(root, 3, 6) == "UURL"
