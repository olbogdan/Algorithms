# 1129. Shortest Path with Alternating Colors
# Medium
# 2.8K
# 149
# Companies
# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
#
#
#
# Example 1:
#
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:
#
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
#
#
# Constraints:
#
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED = "RED"
        BLUE = "BLUE"
        results = [-1 for _ in range(n)]  # can we use [-1]*n?
        q = deque()
        q.append((0, 0, None))  # (node, len to node, color)

        adjRed = defaultdict(list)
        adjBlue = defaultdict(list)
        for a, b in redEdges:
            adjRed[a].append(b)
        for a, b in blueEdges:
            adjBlue[a].append(b)

        visited = set()
        while q:
            node, lenght, color = q.popleft()
            if results[node] == -1:
                results[node] = lenght

            if (color == None or color == RED) and node in adjBlue:
                # add all childs of current node to queue, increment distance + 1
                for child in adjBlue[node]:
                    if (child, BLUE) not in visited:
                        visited.add((child, BLUE))
                        q.append((child, lenght + 1, BLUE))
            if (color == None or color == BLUE) and node in adjRed:
                for child in adjRed[node]:
                    if (child, RED) not in visited:
                        visited.add((child, RED))
                        q.append((child, lenght + 1, RED))

        return results


sol = Solution()
res = sol.shortestAlternatingPaths(3, [[0,1],[1,2]], [])
assert res == [0,1,-1]
res = sol.shortestAlternatingPaths(3, [[0,1],[1,2]], [[1,2]])
assert res == [0,1,2]
