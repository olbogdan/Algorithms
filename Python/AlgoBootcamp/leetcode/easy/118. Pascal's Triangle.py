# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= numRows <= 30
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows-1):
            prevRow = res[-1]
            nextRow = [1]*(len(prevRow)+1)
            for i in range(1, len(prevRow)):
                nextRow[i] = prevRow[i-1] + prevRow[i]
            res.append(nextRow)
        return res


sol = Solution()
assert sol.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert sol.generate(2) == [[1],[1,1]]


class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        # crate array of len nR [1, 1, 1]
        # iterate 1 to len(r) -1 [1, 1(lr), 1]
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [1, 3, 3, 1]
        # [1, 4, 6, 4, 1]

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res = []
        res.append([1])
        res.append([1, 1])

        def dp(row):
            if numRows == row:
                return
            prevArr = res[-1]
            newRow = [1] * (row + 1)
            for i in range(1, len(newRow) - 1):
                newRow[i] = prevArr[i - 1] + prevArr[i]
            res.append(newRow)
            row += 1
            dp(row)

        dp(2)
        return res


sol = Solution2()
assert sol.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert sol.generate(2) == [[1],[1,1]]
