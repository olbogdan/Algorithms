# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#
#
#
# Example 1:
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:
#
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
#
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.
from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minMap = defaultdict(set)
        for r in range(len(matrix)):
            num = float(inf)
            colIdx = -1
            for c in range(len(matrix[0])):
                if matrix[r][c] < num:
                    num = matrix[r][c]
                    colIdx = c
            minMap[colIdx].add(num)
        res = []
        for c in range(len(matrix[0])):
            maxNum = float(-inf)
            for r in range(len(matrix)):
                if matrix[r][c] > maxNum:
                    maxNum = matrix[r][c]
            if maxNum in minMap[c]:
                res.append(maxNum)
        return res


sol = Solution()
print(sol.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(sol.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
