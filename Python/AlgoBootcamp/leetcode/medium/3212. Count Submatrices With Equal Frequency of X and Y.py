# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:
#
# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
#
#
# Example 1:
#
# Input: grid = [["X","Y","."],["Y",".","."]]
#
# Output: 3
#
# Explanation:
#
#
#
# Example 2:
#
# Input: grid = [["X","X"],["X","Y"]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has an equal frequency of 'X' and 'Y'.
#
# Example 3:
#
# Input: grid = [[".","."],[".","."]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has at least one 'X'.
#
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.
from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        diff = [0] * cols
        hasXInCol = [False] * cols
        res = 0

        for r in range(rows):
            currentRowDiff = 0
            rowHasX = False
            for c in range(cols):
                val = grid[r][c]
                if val == 'X':
                    currentRowDiff += 1
                    rowHasX = True
                elif val == 'Y':
                    currentRowDiff -= 1

                diff[c] += currentRowDiff

                if rowHasX:
                    hasXInCol[c] = True

                if diff[c] == 0 and hasXInCol[c]:
                    res += 1

        return res


sol = Solution()
assert sol.numberOfSubmatrices([["X","Y","."],["Y",".","."]]) == 3
assert sol.numberOfSubmatrices([["X","X"],["X","Y"]]) == 0
