# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
#
#
#
# Example 1:
#
#
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Example 2:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Example 3:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
#
#
# Constraints:
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
from cmath import inf
from collections import defaultdict
from heapq import heappush, heappop
from typing import List


# #Bellman-Ford O(V*K)
# iterate k times, in each step fill all accessible nodes val
# create a main array globally and a temp array on each step
# fill temp array


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        permArray = [float(inf)] * n
        permArray[src] = 0
        # Bellman-Ford
        for i in range(k+1):
            tempArray = permArray.copy()
            for fr, to, price in flights:
                if permArray[fr] + price < tempArray[to]:
                    tempArray[to] = permArray[fr] + price
            permArray = tempArray
        if permArray[dst] != float(inf):
            return permArray[dst]
        return -1


sol = Solution()
res = sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
assert res == 700


# #Dijkstra's
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fromCity, toCity, price in flights:
            adj[fromCity].append((price, toCity))
        heap = []
        heap.append((0, -1, src)) # currentPrice, currentK, currentNode
        visited = set()
        while heap:
            cPrice, cK, cNode = heappop(heap)
            if cK > k or (cPrice, cK, cNode) in visited:
                continue
            if cNode == dst:
                return cPrice

            visited.add((cPrice, cK, cNode))
            for neiPrice, neiNode in adj[cNode]:
                heappush(heap, (cPrice+neiPrice, cK+1, neiNode))
        return -1


sol = Solution2()
res = sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
assert res == 700
