# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:
#
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105
from typing import List


from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        ROW, COL = len(mat), len(mat[0])
        result = []

        # Iterate over all possible diagonals
        for d in range(ROW + COL - 1):
            diagonal = []

            # Starting point of this diagonal
            row = 0 if d < COL else d - COL + 1
            col = d if d < COL else COL - 1

            # Walk down-left until out of bounds
            while row < ROW and col >= 0:
                diagonal.append(mat[row][col])
                row += 1
                col -= 1

            # Reverse every second diagonal (to get zig-zag order)
            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)

        return result



sol = Solution()
assert sol.findDiagonalOrder([[1, 2], [3, 4]]) == [1,2,3,4]
assert sol.findDiagonalOrder([[1]]) == [1]
