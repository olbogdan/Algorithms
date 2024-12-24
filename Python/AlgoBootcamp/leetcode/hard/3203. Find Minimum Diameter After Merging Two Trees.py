# There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
#
# You must connect one node from the first tree with another node from the second tree with an edge.
#
# Return the minimum possible diameter of the resulting tree.
#
# The diameter of a tree is the length of the longest path between any two nodes in the tree.
#
#
#
# Example 1:
#
# Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
#
# Output: 3
#
# Explanation:
#
# We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.
#
# Example 2:
#
#
# Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
#
# Output: 5
#
# Explanation:
#
# We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.
#
#
#
# Constraints:
#
# 1 <= n, m <= 105
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
from collections import defaultdict
from typing import List


class Solution:

    def longestPath(self, node, parent, adj) -> List[int]:
        res = []
        for nei in adj[node]:
            if nei == parent:
                continue
            path = self.longestPath(nei, node, adj)
            if (len(path) > len(res)):
                res = path
        res.append(node)
        return res

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def createAdj(edges):
            adj = defaultdict(list)
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj
        adj1 = createAdj(edges1)
        adj2 = createAdj(edges2)

        def optimalLen(adj):
            leaf = self.longestPath(0, -1, adj)[0]
            path = self.longestPath(leaf, -1, adj)
            maxLenOfTree = len(path)
            midPath = maxLenOfTree // 2
            return (midPath, maxLenOfTree-1)
        mid1, width1 = optimalLen(adj1)
        mid2, width2 = optimalLen(adj2)
        res = max(mid1 + mid2 + 1, width1, width2)
        return res



sol = Solution()
assert sol.minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3]], [[0, 1]]) == 3
assert sol.minimumDiameterAfterMerge([[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], [[0,1],[0,2],[0,3]]) == 7
