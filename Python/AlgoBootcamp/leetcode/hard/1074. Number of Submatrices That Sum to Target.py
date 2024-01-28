# Given a matrix and a target, return the number of non-empty submatrices that sum to target.
#
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
#
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
#
#
#
# Example 1:
#
#
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:
#
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:
#
# Input: matrix = [[904]], target = 0
# Output: 0
#
#
# Constraints:
#
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        COLS = len(matrix[0])
        ROWS = len(matrix)
        prefix = [[0] * (COLS) for _ in range(ROWS)]  # 0's row/cols for edge cases
        for r in range(ROWS):
            for c in range(COLS):
                left = prefix[r][c - 1] if c > 0 else 0
                top = prefix[r - 1][c] if r > 0 else 0
                diagonal = prefix[r - 1][c - 1] if min(r, c) > 0 else 0
                cur = matrix[r][c]
                prefix[r][c] = cur + left + top - diagonal

        result = 0
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                memo = defaultdict(int)
                memo[0] = 1
                for c in range(COLS):
                    top = prefix[r1 - 1][c] if r1 > 0 else 0
                    cur = prefix[r2][c]
                    curSum = cur - top
                    dif = curSum - target
                    result += memo[dif]
                    memo[curSum] += 1
        return result


assert Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0) == 4
