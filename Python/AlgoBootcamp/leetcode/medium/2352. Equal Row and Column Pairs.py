# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
#
#
#
# Example 1:
#
#
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:
#
#
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowCounter = {}  # {key: rowHash, val int: reps}

        N = len(grid)
        for r in range(N):
            rowKey = ""
            for c in range(N):
                rowKey += "*"
                rowKey += str(grid[r][c])
            if rowKey in rowCounter:
                rowCounter[rowKey] += 1
            else:
                rowCounter[rowKey] = 1

        result = 0
        for c in range(N):
            colKey = ""
            for r in range(N):
                colKey += "*"
                colKey += str(grid[r][c])
            if colKey in rowCounter:
                result += rowCounter[colKey]

        return result


sol = Solution()
assert sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
