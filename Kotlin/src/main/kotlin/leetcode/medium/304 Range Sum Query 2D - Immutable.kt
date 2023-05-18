package leetcode.medium
/*Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.



Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.*/

class  `304 Range Sum Query 2D - Immutable` (matrix: Array<IntArray>) {
    var board: Array<Array<Int>>

    init {
        val ROWS = matrix.size + 1
        val COLS = matrix[0].size + 1

        // Initialize board with 0s
        board = Array(ROWS) { Array(COLS) { 0 } }

        for (r in 1 until ROWS) {
            for (c in 1 until COLS) {
                val originMatrixVal = matrix[r-1][c-1]
                board[r][c] = originMatrixVal + board[r - 1][c] + board[r][c - 1] - board[r-1][c-1]
            }
        }
    }

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        val r1 = row1 + 1
        val c1 = col1 + 1
        val r2 = row2 + 1
        val c2 = col2 + 1
        val fullRectangle = board[r2][c2]
        val leftPrefix = board[r2][c1 - 1]
        val topPrefix = board[r1 - 1][c2]
        val topleftItem = board[r1 - 1][c1 - 1]
        return fullRectangle - leftPrefix - topPrefix + topleftItem
    }
}
