# You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
#
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
#
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.
#
# Notice that the modulo is performed after getting the maximum product.
#
#
#
# Example 1:
#
#
# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
# Example 2:
#
#
# Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
# Example 3:
#
#
# Input: grid = [[1,3],[0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# -4 <= grid[i][j] <= 4
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        ROW, COL = len(grid), len(grid[0])

        dpMax = [[0] * COL for _ in range(ROW)]
        dpMin = [[0] * COL for _ in range(ROW)]

        dpMax[0][0] = dpMin[0][0] = grid[0][0]

        for r in range(ROW):
            for c in range(COL):
                if r == 0 and c == 0:
                    continue

                val = grid[r][c]
                candidates = []

                if r > 0:
                    candidates.append(dpMax[r - 1][c] * val)
                    candidates.append(dpMin[r - 1][c] * val)

                if c > 0:
                    candidates.append(dpMax[r][c - 1] * val)
                    candidates.append(dpMin[r][c - 1] * val)

                dpMax[r][c] = max(candidates)
                dpMin[r][c] = min(candidates)

        res = dpMax[ROW - 1][COL - 1]
        return res % MOD if res >= 0 else -1


sol = Solution()
assert sol.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]) == -1
assert sol.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]) == 8
