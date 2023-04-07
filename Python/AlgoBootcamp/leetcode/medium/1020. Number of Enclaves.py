# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
#
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # let's modify the grid instead of visited set
        # visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if r == -1 or r == ROWS or c == -1 or c == COLS or grid[r][c] != 1:
                return 0
            res = 1
            # mark as visited by setting grid -1
            grid[r][c] = -1
            for dirR, dirC in directions:
                res += dfs(r + dirR, c + dirC)
            return res

        lend = borderLend = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and grid[r][c] == 1:
                    borderLend += dfs(r, c)
                # count all 1 and -1 lands
                if grid[r][c] != 0:
                    lend += 1
        return lend - borderLend


sol = Solution()
assert sol.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 3
