# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:
#
# Input: matrix = [["0"]]
# Output: 0
# Example 3:
#
# Input: matrix = [["1"]]
# Output: 1
#
#
# Constraints:
#
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
from collections import deque
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        heights = self.convertToHights(matrix)
        for r in range(len(heights)):
            result = max(result, self.getMaxRectangle(heights[r]))
        return result

    def getMaxRectangle(self, heights: List[int]) -> int:
        result = 0
        increasingStack = deque()

        def shrinkStack(rightBorder : int):
            nonlocal result
            while increasingStack:
                index, height = increasingStack.pop()
                result = max(result, height * (rightBorder - index))


        for i in range(len(heights)):
            if heights[i] == 0:
                shrinkStack(i)
            elif len(increasingStack) == 0 or increasingStack[-1][1] <= heights[i]:
                increasingStack.append((i, heights[i]))
            else:
                lastPopped = 0
                # this i element makes stack decreasing, pop stack to make it increasing again
                while increasingStack and increasingStack[-1][1] > heights[i]:
                    index, height = increasingStack.pop()
                    result = max(result, height * (i - index))
                    lastPopped = index

                increasingStack.append((lastPopped, heights[i]))

        shrinkStack(len(heights))
        return result

    def convertToHights(self, matrix: List[List[str]]) -> List[List[int]]:
        result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0:
                    result[0][c] = int(matrix[0][c])
                    continue

                if matrix[r][c] != '0':
                    result[r][c] = result[r - 1][c] + 1
        return result


sol = Solution()
assert sol.maximalRectangle([["0"]]) == 0
assert sol.maximalRectangle([["1"]]) == 1
assert sol.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                              ["1", "0", "0", "1", "0"]]) == 6
