# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:
#
# Input: n = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= n <= 20
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        iterI = 1

        firstRow = firstCol = 0
        lastRow = lastCol = n - 1
        while True:
            for i in range(firstCol, lastCol + 1):
                result[firstRow][i] = iterI
                iterI += 1
            firstRow += 1

            if firstRow > lastRow:
                break

            for i in range(firstRow, lastRow + 1):
                result[i][lastCol] = iterI
                iterI += 1
            lastCol -= 1

            if firstCol > lastCol:
                break
            for i in reversed(range(firstCol, lastCol + 1)):
                result[lastRow][i] = iterI
                iterI += 1
            lastRow -= 1

            for i in reversed(range(firstRow, lastRow + 1)):
                result[i][firstCol] = iterI
                iterI += 1
            firstCol += 1
        return result


sol = Solution()
assert sol.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]
