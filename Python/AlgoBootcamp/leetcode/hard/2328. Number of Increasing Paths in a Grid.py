# You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
#
# Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.
#
# Two paths are considered different if they do not have exactly the same sequence of visited cells.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,1],[3,4]]
# Output: 8
# Explanation: The strictly increasing paths are:
# - Paths with length 1: [1], [1], [3], [4].
# - Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
# - Paths with length 3: [1 -> 3 -> 4].
# The total number of paths is 4 + 3 + 1 = 8.
# Example 2:
#
# Input: grid = [[1],[2]]
# Output: 3
# Explanation: The strictly increasing paths are:
# - Paths with length 1: [1], [2].
# - Paths with length 2: [1 -> 2].
# The total number of paths is 2 + 1 = 3.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 1 <= grid[i][j] <= 105
from cmath import inf
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = {}

        def dp(r, c, prev, visited):
            if min(r, c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] <= prev or (r, c) in visited:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            visited.add((r, c))
            curValue = grid[r][c]
            result = 1
            # go 4 direction dfs to summ with result
            result = (result + dp(r - 1, c, curValue, visited)) % mod
            result = (result + dp(r, c - 1, curValue, visited)) % mod
            result = (result + dp(r + 1, c, curValue, visited)) % mod
            result = (result + dp(r, c + 1, curValue, visited)) % mod
            visited.remove((r, c))
            memo[(r, c)] = result
            return result

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result = (result + dp(r, c, -inf, set())) % mod
        return result


sol = Solution()
res = sol.countPaths([[1],[2]])
assert res == 3
assert sol.countPaths([[1,1],[3,4]]) == 8
