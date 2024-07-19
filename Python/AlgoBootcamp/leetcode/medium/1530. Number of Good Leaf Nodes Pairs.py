# You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
#
# Return the number of good leaf node pairs in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
# Example 3:
#
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 210].
# 1 <= Node.val <= 100
# 1 <= distance <= 10
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        adj = defaultdict(list)
        leafs = set()

        def createAdj(node, parent):
            nonlocal adj
            nonlocal leafs
            if parent:
                adj[node].append(parent)
            if node.left:
                adj[node].append(node.left)
                createAdj(node.left, node)
            if node.right:
                adj[node].append(node.right)
                createAdj(node.right, node)
            if not node.left and not node.right:
                leafs.add(node)

        createAdj(root, None)

        res = 0

        def dfs(node, distance, visited):
            nonlocal res
            if distance < 0 or node in visited:
                return
            if node in leafs:
                res += 1
                return

            visited.add(node)
            distance -= 1
            for nei in adj[node]:
                dfs(nei, distance, visited)

        for leaf in leafs:
            for nei in adj[leaf]:
                visited = set()
                visited.add(leaf)
                dfs(nei, distance - 1, visited)

        return res // 2


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
assert sol.countPairs(root, 3) == 1
