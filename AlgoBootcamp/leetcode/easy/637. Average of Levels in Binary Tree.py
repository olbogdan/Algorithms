# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    stack = deque()
    stack.append(root)
    result = []
    while stack:
        level = []
        for i in range(len(stack)):
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            level.append(node.val)
        result.append(sum(level) / len(level))
    return result


node = TreeNode(10, TreeNode(20), TreeNode(30, TreeNode(40), TreeNode(60)))
assert averageOfLevels(node) == [10, 25, 50]