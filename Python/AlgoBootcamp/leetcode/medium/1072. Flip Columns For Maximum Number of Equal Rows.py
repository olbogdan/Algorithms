# You are given an m x n binary matrix matrix.
#
# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
#
# Return the maximum number of rows that have all values equal after some number of flips.
#
#
#
# Example 1:
#
# Input: matrix = [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:
#
# Input: matrix = [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:
#
# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is either 0 or 1.
from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)

        for row in matrix:
            pattern = tuple(row)
            flipped_pattern = tuple(1 - x for x in row)

            pattern_count[pattern] += 1
            pattern_count[flipped_pattern] += 1

        return max(pattern_count.values())


sol = Solution()
assert sol.maxEqualRowsAfterFlips([[0, 1], [1, 1]]) == 1
assert sol.maxEqualRowsAfterFlips([[0, 1], [1, 0]]) == 2
assert sol.maxEqualRowsAfterFlips([[1,0,0],[1,1,0]]) == 1