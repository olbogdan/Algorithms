# You are given an m x n binary matrix grid.
#
# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
#
# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
#
# Return the highest possible score after making any number of moves (including zero moves).
#
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# Example 2:
#
# Input: grid = [[0]]
# Output: 1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid[i][j] is either 0 or 1.
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        grid = self.flipRowsIfZeroPrefix(grid)
        grid = self.flipZeroColumns(grid)
        result = 0
        for r in range(len(grid)):
            result += self.convertRowToNumber(r, grid)
        return result

    def convertRowToNumber(self, r, grid: List[List[int]]) -> int:
        num = 0
        for c in range(len(grid[0])):
            num = (num << 1) | grid[r][c]
        return num

    def flipRowsIfZeroPrefix(self, grid: List[List[int]]) -> List[List[int]]:
        for r in range(len(grid)):
            if grid[r][0] == 0:
                for c in range(len(grid[0])):
                    grid[r][c] = 0 if grid[r][c] else 1
        return grid

    def flipZeroColumns(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])

        def countZeros(c) -> int:
            zeros = 0
            for r in range(ROWS):
                if grid[r][c] == 0:
                    zeros += 1
            return zeros

        def flipColumn(c):
            for r in range(ROWS):
                grid[r][c] = 0 if grid[r][c] else 1

        for c in range(COLS):
            zeros = countZeros(c)
            if zeros > ROWS // 2:
                flipColumn(c)
        return grid


sol = Solution()
assert sol.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39
assert sol.matrixScore([[0]]) == 1
