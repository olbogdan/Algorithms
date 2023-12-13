# Given an m x n binary matrix mat, return the number of special positions in mat.
#
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
#
#
#
# Example 1:
#
#
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:
#
#
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        memoR = [0] * rows
        memoC = [0] * cols

        for r in range(rows):
            for c in range(cols):
                memoR[r] += mat[r][c]
                if memoR[r] > 1:
                    break
        for c in range(cols):
            for r in range(rows):
                memoC[c] += mat[r][c]
                if memoC[c] > 1:
                    break

        result = 0
        for r in range(rows):
            if memoR[r] > 1 or memoR[r] == 0:
                continue
            for c in range(cols):
                if memoC[c] > 1 or memoC[c] == 0:
                    continue
                if mat[r][c] == 1:
                    result += 1
        return result


sol = Solution()
assert sol.numSpecial([[1,0,0],[0,0,1],[1,0,0]]) == 1
