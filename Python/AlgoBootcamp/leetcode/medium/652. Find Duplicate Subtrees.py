# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with the same node values.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:
#
#
# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:
#
#
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#
#
# Constraints:
#
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo = defaultdict(int)
        result = []

        def dfs(node):
            if not node:
                return "n"
            key = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            memo[key] += 1
            if memo[key] == 2:
                result.append(node)
            return key

        dfs(root)
        return result


node = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3))
sol = Solution()
res = sol.findDuplicateSubtrees(node)
assert len(res) == 1
assert res[0].val == 3
