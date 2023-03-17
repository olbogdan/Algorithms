import org.junit.jupiter.api.Assertions

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

fun matrixRecursive(size: Int): List<List<Int>> {
    val matrix = MutableList<MutableList<Int>>(size) { MutableList<Int>(size) { -1 } }

    fun recursive(firstRow: Int, firstColumn: Int, startValue: Int, innerSize: Int) {
        if (startValue > size * size) {
            return
        }
        var currentValue = startValue
        val lastColumn = firstColumn + innerSize - 1
        for (i in firstColumn..lastColumn) {
            matrix[firstRow][i] = currentValue
            currentValue += 1
        }

        val lastRow = firstRow + innerSize - 1
        for (i in firstRow + 1..lastRow) {
            matrix[i][lastColumn] = currentValue
            currentValue += 1
        }

        for (i in lastColumn - 1 downTo firstColumn) {
            matrix[lastRow][i] = currentValue
            currentValue += 1
        }

        for (i in lastRow - 1 downTo firstRow + 1) {
            matrix[i][firstColumn] = currentValue
            currentValue += 1
        }
        recursive(firstRow + 1, firstColumn + 1, currentValue, innerSize - 2)
    }

    recursive(0, 0, 1, size)

    return matrix
}

fun matrix(n: Int): List<List<Int>> {
    val matrix = MutableList<MutableList<Int>>(n) { MutableList<Int>(n) { -1 } }

    var number = 1
    var endRow = n - 1
    var endColumn = n - 1
    var startRow = 0
    var startColumn = 0

    while (number <= n * n) {
        for (column in startColumn..endColumn) {
            matrix[startRow][column] = number
            number += 1
        }
        startRow += 1
        for (row in startRow..endRow) {
            matrix[row][endColumn] = number
            number += 1
        }
        endColumn -= 1
        for (column in (startColumn..endColumn).reversed()) {
            matrix[endRow][column] = number
            number += 1
        }
        endRow -= 1
        for (row in (startRow..endRow).reversed()) {
            matrix[row][startColumn] = number
            number += 1
        }
        startColumn += 1
    }
    return matrix
}

fun main() {
    println(matrixRecursive(5))
    Assertions.assertTrue(matrixRecursive(3) == listOf(listOf(1, 2, 3), listOf(8, 9, 4), listOf(7, 6, 5)))

    println(matrix(5))
    Assertions.assertTrue(matrix(3) == listOf(listOf(1, 2, 3), listOf(8, 9, 4), listOf(7, 6, 5)))
}