# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
from cmath import inf
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = [float(inf)] * (COLS + 1)
        memo[COLS - 1] = 0
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                memo[c] = grid[r][c] + min(memo[c + 1], memo[c])
        return memo[0]


sol = Solution()
res = sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
assert res == 7
res = sol.minPathSum([[1,2,3],[4,5,6]])
assert res == 12


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = [ [float(inf) for _ in range(COLS+1) ] for _ in range(ROWS+1) ]
        for r in range(1, ROWS+1):
            for c in range(1, COLS+1):
                if r == 1 and c == 1:
                    memo[r][c] = grid[0][0]
                else:
                    memo[r][c] = grid[r-1][c-1] + min(memo[r-1][c], memo[r][c-1])
        return memo[-1][-1]


sol = Solution2()
res = sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
assert res == 7
res = sol.minPathSum([[1,2,3],[4,5,6]])
assert res == 12


class Solution3:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        ROWS = len(grid)
        COLS = len(grid[0])
        def dp(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            elif r == ROWS or c == COLS:
                return float(inf)
            else:
                if (r, c) in memo:
                    return memo[(r, c)]
                val = grid[r][c] + min(dp(r+1, c), dp(r, c+1))
                memo[(r, c)] = val
                return val
        return dp(0, 0)


sol = Solution3()
res = sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
assert res == 7
res = sol.minPathSum([[1,2,3],[4,5,6]])
assert res == 12
