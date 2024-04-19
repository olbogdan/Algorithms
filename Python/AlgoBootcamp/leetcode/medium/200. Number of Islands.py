# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if (min(r, c) >= 0
            and r < len(grid)
            and c < len(grid[0])
            and grid[r][c] == '1'):
                grid[r][c] = None
                for shftR, shftC in directions:
                    dfs(r + shftR, c + shftC)

        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    result += 1
                    dfs(r, c)
        return result


solution = Solution()
assert solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1
assert solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3
assert solution.numIslands([["1","0","0","0","0"],["0","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 4
assert solution.numIslands([["1","1","0","0","0"],["0","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3