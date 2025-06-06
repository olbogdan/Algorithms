# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
#
# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
#
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
#
# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
#
#
#
# Example 1:
#
#
#
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
# Example 2:
#
#
#
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
#
#
# Constraints:
#
# n == colors.length
# m == edges.length
# 1 <= n <= 105
# 0 <= m <= 105
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        N = len(colors)
        adj = defaultdict(list)
        inDegree = [0] * N

        for fromNode, toNode in edges:
            adj[fromNode].append(toNode)
            inDegree[toNode] += 1

        dp = [[0] * 26 for _ in range(N)]
        queue = deque()

        for node in range(N):
            if inDegree[node] == 0:
                queue.append(node)
                colorIndex = ord(colors[node]) - ord('a')
                dp[node][colorIndex] = 1

        visit = 0
        while queue:
            node = queue.popleft()
            visit += 1
            for nei in adj[node]:
                neiColorIndex = ord(colors[nei]) - ord('a')
                for color, count in enumerate(dp[node]):
                    dp[nei][color] = max(dp[nei][color], count + (1 if neiColorIndex == color else 0))
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)

        if visit < N:
            return -1

        return max(max(row) for row in dp)


sol = Solution()
assert sol.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
assert sol.largestPathValue("a", [[0, 0]]) == -1
assert sol.largestPathValue("iivvvvv", [[0,1],[1,2],[1,3],[2,3],[3,4],[2,4],[3,5],[1,5],[4,5],[5,6]]) == 5
