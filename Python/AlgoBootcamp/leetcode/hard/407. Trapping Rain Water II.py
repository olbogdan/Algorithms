# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# Example 2:
#
#
# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
#
#
# Constraints:
#
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 104
from heapq import heappush, heappop
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROW = len(heightMap)
        COL = len(heightMap[0])
        if min(ROW, COL) < 3:
            return 0
        heap = []
        for r in range(ROW):
            for c in range(COL):
                if min(r, c) == 0 or r == ROW-1 or c == COL-1:
                    heappush(heap, (heightMap[r][c], r, c))
                    # mark visited
                    heightMap[r][c] = None
        res = 0
        maxHeight = 0
        while heap:
            height, r, c = heappop(heap)
            maxHeight = max(maxHeight, height)
            res += maxHeight - height
            nei = [(r-1, c), (r+1, c), (r,c-1), (r,c+1)]
            for neiR, neiC in nei:
                if min(neiR, neiC) < 0 or neiR == ROW or neiC == COL or heightMap[neiR][neiC] is None:
                    continue
                heappush(heap, (heightMap[neiR][neiC], neiR, neiC))
                heightMap[neiR][neiC] = None
        return res


sol = Solution()
assert sol.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) == 4
assert sol.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]) == 10
