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
        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        def dfs(x, y):
            if (x < 0
                    or y < 0
                    or x > rows - 1
                    or y > columns - 1
                    or (x, y) in visited
                    or grid[x][y] == "0"
            ):
                return
            visited.add((x, y))
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        def toggleVisitedIsland():
            for x, y in visited:
                grid[x][y] = "0"
            visited.clear()

        result = 0
        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == "1":
                    result += 1
                    dfs(x, y)
                    toggleVisitedIsland()
        return result


solution = Solution()
assert solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1
assert solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3
assert solution.numIslands([["1","0","0","0","0"],["0","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 4
assert solution.numIslands([["1","1","0","0","0"],["0","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3