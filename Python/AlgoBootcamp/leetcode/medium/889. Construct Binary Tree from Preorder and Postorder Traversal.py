# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
#
# If there exist multiple answers, you can return any of them.
#
#
#
# Example 1:
#
#
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# Example 2:
#
# Input: preorder = [1], postorder = [1]
# Output: [1]
#
#
# Constraints:
#
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        postToIdx = {}  # node : idx
        for idx, num in enumerate(postorder):
            postToIdx[num] = idx

        def build(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None
            root = TreeNode(val=preorder[i1])
            # if subarray is > 0
            if i1 != i2:
                leftVal = preorder[i1 + 1]
                mid = postToIdx[leftVal]
                leftSubtreeSize = mid - j1 + 1
                root.left = build(i1 + 1, i1 + leftSubtreeSize, j1, mid)
                root.right = build(i1 + leftSubtreeSize + 1, i2, mid + 1, j2 - 1)
            return root

        return build(0, N - 1, 0, N - 1)

