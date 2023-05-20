# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
#
#
# Example 1:
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
# Constraints:
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a/b == 2 * b/c == 3 -> a/c == 6 or c/a == 1/6
        # path from a to b with weight 3
        adj = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            weight = values[i]
            adj[a].append([b, weight])
            adj[b].append([a, 1 / weight])

        # bfs from a to c,  a - (2) - b - (3) - c == multiply edges 2*3
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            queue = deque()
            queue.append((src, 1))
            visited = {src}
            while queue:
                node, curWeight = queue.popleft()
                if node == target:
                    return curWeight
                for neiNode, neiWeight in adj[node]:
                    if neiNode not in visited:
                        visited.add(neiNode)
                        queue.append((neiNode, curWeight * neiWeight))
            return -1

        return [bfs(a, b) for a, b in queries]


sol = Solution()
res = sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
assert res == [6.00000,0.50000,-1.00000,1.00000,-1.00000]
