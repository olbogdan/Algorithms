# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]
# Example 3:
#
# Input: rowIndex = 1
# Output: [1,1]
#
#
# Constraints:
#
# 0 <= rowIndex <= 33
#
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [1, 3, 3, 1]
        if rowIndex == 0:
            return [1]
        level = [1]
        for i in range(rowIndex):
            nextLevel = []
            for j in range(i + 2):
                num = 0
                if j > 0:
                    num += level[j - 1]
                if j < len(level):
                    num += level[j]
                nextLevel.append(num)
            level = nextLevel
        return level
