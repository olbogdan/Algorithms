# You are given an n x n integer matrix. You can do the following operation any number of times:
#
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
#
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:
#
#
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105
from cmath import inf
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        minVal = float(inf)
        negativeNums = 0
        for row in matrix:
            for item in row:
                absItem = abs(item)
                totalSum += absItem
                negativeNums += 1 if item < 0 else 0
                if absItem < minVal:
                    minVal = absItem
        odd = negativeNums & 1 == 1
        # minVal initially 100% was less than 0, but we added it as +
        # so we need to remove this plus
        # and also we need to deduct this num sinc it will remain - after swipes
        if odd:
            totalSum -= (minVal*2)
        return totalSum


sol = Solution()
assert sol.maxMatrixSum([[1, -1], [-1, 1]]) == 4
assert sol.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
assert sol.maxMatrixSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45
