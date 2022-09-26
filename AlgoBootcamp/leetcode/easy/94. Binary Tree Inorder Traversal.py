# # Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversalIterative(root: Optional[TreeNode]) -> [int]:
    result = []
    stack = deque()
    pointer = root
    while stack or pointer:
        if pointer:
            stack.append(pointer)
            pointer = pointer.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            pointer = cur.right
    return result


node = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
assert inorderTraversalIterative(node) == [1, 3, 2]


def inorderTraversal(root: Optional[TreeNode]) -> [int]:
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


node = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
assert inorderTraversal(node) == [1, 3, 2]


def inorderTraversalIterative2(root: Optional[TreeNode]) -> [int]:
    if not root:
        return []
    visited = set()
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        left = queue[-1].left
        if left and left not in visited:
            queue.append(left)
            visited.add(left)
        else:
            node = queue.pop()
            result.append(node.val)
            if node.right:
                queue.append(node.right)

    return result


node = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
assert inorderTraversalIterative2(node) == [1, 3, 2]