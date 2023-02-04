# Description
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# Example
# Example 1:
#
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.
# Example 2:
#
# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.


from typing import (
    List,
)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1 part check if no circles
        # 2 part check if all nodes are connected
        if not n:
            return True
        visited = set()
        adj = { i:[] for i in range(n) }
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


sol = Solution()
assert sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
assert sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
