package leetcode.medium
/*Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100*/

class `54 Spiral Matrix` {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        var firstRow = 0
        var firstCol = 0
        var lastRow = matrix.size - 1
        var lastCol = matrix[0].size - 1
        val result = mutableListOf<Int>()

        while (firstRow <= lastRow && firstCol <= lastCol) {
            for (i in firstCol..lastCol) {
                result.add(matrix[firstRow][i])
            }
            firstRow++

            if (firstRow > lastRow) {
                break
            }

            for (i in firstRow..lastRow) {
                result.add(matrix[i][lastCol])
            }
            lastCol--

            if (firstCol > lastCol) {
                break
            }

            for (i in lastCol downTo firstCol) {
                result.add(matrix[lastRow][i])
            }
            lastRow--

            for (i in lastRow downTo firstRow) {
                result.add(matrix[i][firstCol])
            }
            firstCol++
        }

        return result
    }
}
