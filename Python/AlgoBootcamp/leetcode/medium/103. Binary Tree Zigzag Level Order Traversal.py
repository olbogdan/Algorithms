# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]

    result = []
    queue = deque()
    queue.append(root)
    reverse = False
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.val)
        if reverse:
            level.reverse()
        reverse = not reverse
        result.append(level)
    return result


node = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
assert zigzagLevelOrder(node) == [[1], [3, 2], [4, 5]]