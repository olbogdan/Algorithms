# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
#
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
#
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:
#
#
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
#
#
# Constraints:
#
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n
from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ROWS = m
        COLS = n
        MOD = 10 ** 9 + 7

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        @cache
        def dp(r, c, cap):
            if cap < 0:
                return 0
            elif min(r, c) == -1 or r == ROWS or c == COLS:
                return 1

            result = 0
            for rOffset, cOffset in directions:
                result += dp(r + rOffset, c + cOffset, cap - 1)
            return result % MOD

        return dp(startRow, startColumn, maxMove)


sol = Solution()
assert sol.findPaths(1, 3, 3, 0, 1) == 12
