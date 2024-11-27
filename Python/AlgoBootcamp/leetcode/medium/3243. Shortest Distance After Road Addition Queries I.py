# You are given an integer n and a 2D integer array queries.
#
# There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
#
# queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.
#
# Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.
#
#
#
# Example 1:
#
# Input: n = 5, queries = [[2,4],[0,2],[0,4]]
#
# Output: [3,2,1]
#
# Explanation:
#
#
#
# After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
#
#
#
# After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.
#
#
#
# After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.
#
# Example 2:
#
# Input: n = 4, queries = [[0,3],[0,2]]
#
# Output: [1,1]
#
# Explanation:
#
#
#
# After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.
#
#
#
# After the addition of the road from 0 to 2, the length of the shortest path remains 1.
#
#
#
# Constraints:
#
# 3 <= n <= 500
# 1 <= queries.length <= 500
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# There are no repeated roads among the queries.
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, N: int, queries: List[List[int]]) -> List[int]:
        adj = (defaultdict(list))
        for i in range(0, N-1):
            adj[i].append(i+1)
        res = []
        for queryA, queryB in queries:
            adj[queryA].append(queryB)
            heap = [] # (len, nodeId)
            heapq.heappush(heap, (0, 0))
            visited = set()
            while heap:
                curLen, curNodeId = heapq.heappop(heap)
                if curNodeId == N-1:
                    res.append(curLen)
                    break
                if curNodeId in visited:
                    continue
                visited.add(curNodeId)
                for neiId in adj[curNodeId]:
                    heapq.heappush(heap, (curLen+1, neiId))
        return res


sol = Solution()
assert sol.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]) == [3,2,1]
assert sol.shortestDistanceAfterQueries(4, [[0,3],[0,2]]) == [1,1]
assert sol.shortestDistanceAfterQueries(3, [[0,2],[0,1]]) == [1,1]
