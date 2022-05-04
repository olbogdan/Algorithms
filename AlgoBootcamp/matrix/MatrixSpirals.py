def matrix(n):
    matrix = [[-1] * n for i in range(n)]
    count = 1
    startRow = 0
    startColumn = 0
    endRow = n - 1
    endColumn = n - 1
    while count <= n*n:
        for column in range(startColumn, endColumn+1):
            matrix[startRow][column] = count
            count += 1
        startRow += 1
        for row in range(startRow, endRow+1):
            matrix[row][endColumn] = count
            count += 1
        endColumn -= 1
        for column in range(endColumn, startColumn-1, -1):
            matrix[endRow][column] = count
            count += 1
        endRow -= 1
        for row in range(endRow, startRow-1, -1):
            matrix[row][startColumn] = count
            count += 1
        startColumn += 1
    return matrix


print(matrix(3))
assert(matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
