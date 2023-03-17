/// Write a function that accepts an integer N
/// and returns a NxN spiral matrix.
/// Example:
///  matrix(2)
///         [[1, 2],
///         [4,3]]
///
///  matrix(3)
///     [[1, 2, 3],
///     [8, 9, 4],
///     [7, 6, 5]]
///
///  matrix(4)
///  [[1, 2, 3, 4],
///  [12, 13, 14, 5],
///  [11, 16, 15, 6],
///  [10, 9, 8, 7]]

import Foundation

func matrix(_ n: Int) -> [[Int]] {
    var matrix: [[Int]] = Array.init(
        repeating: Array.init(repeating: -1, count: n),
        count: n
    )
    var number = 1
    var endRow = n-1
    var endColumn = n-1
    var startRow = 0
    var startColumn = 0

    while number <= n*n {

        for column in stride(from:startColumn, through: endColumn, by: 1) {
            matrix[startRow][column] = number
            number += 1
        }
        startRow += 1

        // startRow ... endRow - thorws Fatal error: Range requires lowerBound <= upperBound.
        // use `stride()` instead
        for row in stride(from: startRow, through: endRow, by: 1) {
            matrix[row][endColumn] = number
            number += 1
        }
        endColumn -= 1

        for column in stride(from: startColumn, through: endColumn, by: 1).reversed() {
            matrix[endRow][column] = number
            number += 1
        }
        endRow -= 1

        for row in stride(from: startRow, through: endRow, by: 1).reversed() {
            matrix[row][startColumn] = number
            number += 1
        }
        startColumn += 1
    }
    return matrix
}


assert(matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(matrix(3))
