# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
#
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
#
# Note that the nodes have no values and that we only use the node numbers in this problem.
#
#
#
# Example 1:
#
#
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# Example 2:
#
#
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# Example 3:
#
#
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
#
#
# Constraints:
#
# n == leftChild.length == rightChild.length
# 1 <= n <= 104
# -1 <= leftChild[i], rightChild[i] <= n - 1


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        presentedNodes = set(leftChild + rightChild)
        presentedNodes.discard(-1)  # remove null node
        if len(presentedNodes) == n:
            return False  # all nodes have parents, the tree is invalid

        root = None
        for i in range(n):
            # find any node witout parents
            if i not in presentedNodes:
                root = i
                break

        visited = set()

        def dfs(i):
            # leaf with no childs, reached the end
            if i == -1:
                return True
            # cycle
            if i in visited:
                return False
            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])

        return dfs(root) and len(visited) == n