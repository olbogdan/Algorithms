# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    array = []
    for sub in matrix:
        array.extend(sub)

    l, r = 0, len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] > target:
            r = mid - 1
        elif array[mid] < target:
            l = mid + 1
        else:
            return True
    return False


assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) is True
assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60) is True
assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 100) is False
