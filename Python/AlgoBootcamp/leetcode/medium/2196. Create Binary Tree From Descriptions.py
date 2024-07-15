# You are given a 2D integer array descriptions where descriptions[i]
# = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values.
# Furthermore,
#
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
#
# The test cases will be generated such that the binary tree is valid.
#
#
#
# Example 1:
#
#
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
# Example 2:
#
#
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
#
#
# Constraints:
#
# 1 <= descriptions.length <= 104
# descriptions[i].length == 3
# 1 <= parenti, childi <= 105
# 0 <= isLefti <= 1
# The binary tree described by descriptions is valid.
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        potentialRoots = set()
        for r, _, _ in descriptions:
            potentialRoots.add(r)

        adj = defaultdict(list)
        for parent, child, isLeft in descriptions:
            adj[parent].append((child, isLeft))
            if child in potentialRoots:
                potentialRoots.remove(child)

        def dfs(nodeVal):
            nonlocal adj
            node = TreeNode(val=nodeVal)
            for child, isLeft in adj[nodeVal]:
                if isLeft == 1:
                    node.left = dfs(child)
                else:
                    node.right = dfs(child)
            return node

        rootVal = list(potentialRoots)[0]
        return dfs(rootVal)


sol = Solution()
assert sol.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
assert sol.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]])
