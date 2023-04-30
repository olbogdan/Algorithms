# Alice and Bob have an undirected graph of n nodes and three types of edges:
#
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
#
# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
#
#
#
# Example 1:
#
#
#
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:
#
#
#
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:
#
#
#
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
#
#
#
#
# Constraints:
#
# 1 <= n <= 105
# 1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= typei <= 3
# 1 <= ui < vi <= n
# All tuples (typei, ui, vi) are distinct.
from typing import List


class UF:
    def __init__(self, N):
        self.n = N
        self.parents = [i for i in range(N + 1)]
        self.rank = [1] * (N + 1)

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    # returns 0 if nodes are already connected, else 1
    def union(self, i, j):
        iParent, jParent = self.find(i), self.find(j)
        if iParent == jParent:
            return 0

        if self.rank[iParent] > self.rank[jParent]:
            self.rank[iParent] += self.rank[jParent]
            self.parents[jParent] = iParent
        else:
            self.rank[jParent] += self.rank[iParent]
            self.parents[iParent] = jParent
        self.n -= 1
        return 1

    def isConnected(self):
        return self.n == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alise = UF(n)
        bob = UF(n)

        # lets count needed connections instead of removing them from edges
        connections = 0

        # take all universal edges
        for type, u, v in edges:
            if type == 3:
                # adds connectin if not added
                # increments connections if at least one new connection was added
                connections += (alise.union(u, v) | bob.union(u, v))

        # take any personal connection, if connection between edges does not exist yet
        for type, u, v in edges:
            if type == 1:
                connections += alise.union(u, v)
            if type == 2:
                connections += bob.union(u, v)

        if alise.isConnected() and bob.isConnected():
            return len(edges) - connections
        return -1


sol = Solution()
assert sol.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]) == 0
