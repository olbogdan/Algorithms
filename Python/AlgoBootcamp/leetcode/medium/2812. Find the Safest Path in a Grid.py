# You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
#
# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.
#
# The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.
#
# Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
#
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.
#
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
# Output: 0
# Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
# Example 2:
#
#
# Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.
# Example 3:
#
#
# Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
# - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.
#
#
# Constraints:
#
# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.
from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        starts = self.findStarts(grid)
        safetyMap = self.createSafetyMap(len(grid), len(grid[0]), starts)
        return self.findSafestPathScore(safetyMap)

    def findSafestPathScore(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = float("inf")
        pq = []  # max heap
        pq.append((-grid[0][0], 0, 0))  # distance to danger, r, c
        safest = INF
        # reuse grid INF as visited
        grid[0][0] = INF
        while pq:
            dist, r, c = heappop(pq)
            safest = min(safest, abs(dist))
            # shortcut, 0 lowest safety possible
            if safest == 0 or (r == ROWS - 1 and c == COLS - 1):
                return safest
            for rSh, cSh in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                newR = r + rSh
                newC = c + cSh
                if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] == INF:
                    continue
                nextDist = -min(abs(dist), grid[newR][newC])
                heappush(pq, (nextDist, newR, newC))
                grid[newR][newC] = INF
        return safest

    def createSafetyMap(self, ROWS: int, COLS: int, starts: List[List[int]]) -> List[List[int]]:
        INF = float("inf")
        result = [[INF] * COLS for _ in range(ROWS)]
        q = deque()
        for r, c in starts:
            q.append([r, c])  # row, col
        dist = 0  # distance to danger
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r >= ROWS or c >= COLS or result[r][c] != INF:
                    continue
                result[r][c] = dist
                for rSh, cSh in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    q.append([r + rSh, c + cSh])
            dist += 1
        return result

    def findStarts(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    result.append([r, c])
        return result


sol = Solution()
# assert sol.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
# assert sol.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2
# assert sol.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]) == 2
assert sol.maximumSafenessFactor([[0,1,1],[0,0,1],[1,0,0]]) == 1