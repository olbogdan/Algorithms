# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
#
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
#
#
#
# Example 1:
#
#
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# Example 2:
#
#
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# Example 3:
#
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
# matrix[i][j] is either 0 or 1.
from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Calculate heights for each column
        for r in range(1, ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        res = 0
        for r in range(ROWS):
            # Sort the heights in ascending order
            matrix[r].sort()

            # Iterate through the sorted heights
            for c in range(COLS):
                height = matrix[r][c]
                width = COLS - c
                res = max(res, height * width)

        return res


sol = Solution()
assert sol.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]) == 4
