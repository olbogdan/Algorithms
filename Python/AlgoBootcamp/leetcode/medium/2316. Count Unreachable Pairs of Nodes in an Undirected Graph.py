# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
#
# Return the number of pairs of different nodes that are unreachable from each other.
#
#
#
# Example 1:
#
#
# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
# Example 2:
#
#
# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each other:
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
# Therefore, we return 14.
#
#
# Constraints:
#
# 1 <= n <= 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated edges.
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        components = []
        visited = set()

        currentNodeCount = 0

        def dfs(node):
            nonlocal currentNodeCount
            for nei in adj[node]:
                if nei in visited:
                    continue
                currentNodeCount += 1
                visited.add(nei)
                dfs(nei)

        for i in range(n):
            if i in visited:
                continue
            currentNodeCount = 1
            # REMINDER: REMEMBER THIS LINE
            visited.add(i)
            dfs(i)
            components.append(currentNodeCount)

        res = 0
        for c in components:
            res = res + (c * (n - c))
            n -= c
        return res


sol = Solution()
res = sol.countPairs(3, [[0,1],[0,2],[1,2]])
assert res == 0
res = sol.countPairs(3, [[0,1],[2,2]])
assert res == 2
res = sol.countPairs(12, [])
assert res == 66
