# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.
#
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:
#
#
# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
#
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        ln = len(grid)
        for r in range(ln):
            for c in range(ln):
                if grid[r][c] == 1:
                    q.append((r, c))
        if len(q) == 0 or len(q) == 2 * ln:
            return -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxDistance = 0
        while q:
            r, c = q.popleft()
            for dR, dC in directions:
                newR, newC = r + dR, c + dC
                if min(newR, newC) >= 0 and max(newR, newC) < ln and grid[newR][newC] == 0:
                    q.append((newR, newC))
                    grid[newR][newC] = grid[r][c] + 1
                    maxDistance = grid[newR][newC]
        return maxDistance - 1 # -1 bacause we start count from 1(land) and not from 0


sol = Solution()
assert sol.maxDistance([[1,0,0],[0,0,0],[0,0,0]]) == 4
assert sol.maxDistance([[1,0,1],[0,0,0],[1,0,1]]) == 2
