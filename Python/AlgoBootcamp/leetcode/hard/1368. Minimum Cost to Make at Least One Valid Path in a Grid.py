# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
#
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.
#
# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
#
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
#
# Return the minimum cost to make the grid have at least one valid path.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
# Example 2:
#
#
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
# Example 3:
#
#
# Input: grid = [[1,2],[4,3]]
# Output: 1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# 1 <= grid[i][j] <= 4
from heapq import heappush, heappop
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def getAdditionalCost(freeDirection, targetDirection):
            if (freeDirection == 1 and targetDirection[1] == 1
                    or freeDirection == 2 and targetDirection[1] == -1
                    or freeDirection == 3 and targetDirection[0] == 1
                    or freeDirection == 4 and targetDirection[0] == -1):
                return 0
            else:
                return 1

        ROW = len(grid)
        COL = len(grid[0])
        heap = []
        heap.append((0, 0, 0))  # cost, row, col
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        while heap:
            cost, row, col = heappop(heap)
            if row == ROW - 1 and col == COL - 1:
                return cost
            if min(row, col) < 0 or row == ROW or col == COL or (row, col) in visited:
                continue
            visited.add((row, col))
            for shR, shC in direction:
                newCost = cost + getAdditionalCost(grid[row][col], (shR, shC))
                heappush(heap, (newCost, row + shR, col + shC))


sol = Solution()
assert sol.minCost([[1,1,3],[3,2,2],[1,1,4]]) == 0
assert sol.minCost([[1,2],[4,3]]) == 1
assert sol.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]) == 3

