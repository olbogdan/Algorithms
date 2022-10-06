# Given a binary tree root, a node X in the tree is named good if in the path from root
# to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
#
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
#
# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    count = 1

    def dfs(node, topBorder):
        if not node:
            return
        nonlocal count
        if node.val >= topBorder:
            count += 1
        topBorder = max(topBorder, node.val)
        dfs(node.left, topBorder)
        dfs(node.right, topBorder)

    dfs(root.left, root.val)
    dfs(root.right, root.val)
    return count


assert goodNodes(TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3, TreeNode(4))))) == 5
assert goodNodes(TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3, TreeNode(1))))) == 4
