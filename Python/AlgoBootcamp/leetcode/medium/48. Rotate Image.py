# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Constraints:
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: [[int]]):
        left = top = 0
        bottom = right = len(matrix) - 1

        offset = 0
        while True:
            if left > right:
                break
            # upade bounderies
            if left + offset >= right:
                left += 1
                right -= 1
                top += 1
                bottom -= 1
                offset = 0
                continue

            memo = matrix[top][left + offset]

            matrix[top][left + offset] = matrix[bottom - offset][left]
            matrix[bottom - offset][left] = matrix[bottom][right - offset]
            matrix[bottom][right - offset] = matrix[top + offset][right]
            matrix[top + offset][right] = memo

            offset += 1
        return matrix


sol = Solution()
assert sol.rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
assert sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
