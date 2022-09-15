# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:
#
# Input: root = [1,null,2]
# Output: 2
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepthRecursive(root: TreeNode) -> int:
    if not root:
        return 0

    count = 1
    left = maxDepthRecursive(root.left)
    right = maxDepthRecursive(root.right)
    return count + max(left, right)



node = TreeNode(0, left=TreeNode(left=TreeNode(0, None, None)), right=None)
assert maxDepthRecursive(node) == 3


def maxDepthbfs(root: [TreeNode]) -> int:
    if not root:
        return 0
    bfs = 0
    qu = deque([root])
    while qu:
        for i in range(len(qu)):
            node = qu.popleft()
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)
        bfs += 1
    return bfs


node = TreeNode(0, left=TreeNode(left=TreeNode(0, None, None)), right=None)
assert maxDepthbfs(node) == 3