# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []
        while left <= right and top <= bottom:
            for i in range(0, right - left+1):
                result.append(matrix[top][left + i])

            for i in range(1, bottom - top+1):
                result.append(matrix[top + i][right])

            if top != bottom:
                for i in range(1, right - left):
                    result.append(matrix[bottom][right - i])

            if left != right:
                for i in range(0, bottom - top):
                    result.append(matrix[bottom - i][left])

            top += 1
            left += 1
            right -= 1
            bottom -= 1

        return result


sol = Solution()
assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
