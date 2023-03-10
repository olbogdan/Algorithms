# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
#
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
#
#
#
# Example 1:
#
#
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
#
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:
#
# Input: matrix = [[1]]
# Output: 1
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if min(r, c) < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 0
            cur = matrix[r][c]
            res = max(res, 1 + dfs(r - 1, c, cur))
            res = max(res, 1 + dfs(r + 1, c, cur))
            res = max(res, 1 + dfs(r, c - 1, cur))
            res = max(res, 1 + dfs(r, c + 1, cur))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())


sol = Solution()
assert sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
assert sol.longestIncreasingPath([[1]]) == 1
