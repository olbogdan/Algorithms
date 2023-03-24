# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
#
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
#
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
#
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
#
# It's guaranteed that each city can reach city 0 after reorder.
#
#
#
# Example 1:
#
#
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 2:
#
#
# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 3:
#
# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
#
#
# Constraints:
#
# 2 <= n <= 5 * 104
# connections.length == n - 1
# connections[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list) # original direction
        dirrections = set()
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            dirrections.add((a, b))
        visited = {0}
        result = 0

        def dfs(node):
            nonlocal result
            visited.add(node)
            for nei in adj[node]:
                if nei in visited:
                    continue
                # wrong direction, should be reversed
                if (node, nei) in dirrections:
                    result += 1
                dfs(nei)

        dfs(0)
        return result


sol = Solution()
res = sol.minReorder(2, [[0, 1]])
assert res == 1
