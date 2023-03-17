# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

def setZeroes(matrix: [[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeroRow = False
    zeroColumn = False

    for r in range(0, len(matrix)):
        if matrix[r][0] == 0:
            zeroColumn = True
            break
    for c in range(0, len(matrix[0])):
        if matrix[0][c] == 0:
            zeroRow = True
            break

    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for r in range(1, len(matrix)):
        if matrix[r][0] == 0:
            for c in range(1, len(matrix[0])):
                matrix[r][c] = 0

    for c in range(1, len(matrix[0])):
        if matrix[0][c] == 0:
            for r in range(1, len(matrix)):
                matrix[r][c] = 0

    if zeroRow:
        for c in range(0, len(matrix[0])):
            matrix[0][c] = 0

    if zeroColumn:
        for r in range(0, len(matrix)):
            matrix[r][0] = 0

arr = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(arr)
assert arr == [[1,0,1],[0,0,0],[1,0,1]]
