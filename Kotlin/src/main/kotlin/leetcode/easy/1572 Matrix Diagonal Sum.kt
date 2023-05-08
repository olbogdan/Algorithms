package leetcode.easy
/*Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.



Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5


Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
*/
class `1572 Matrix Diagonal Sum` {
    fun diagonalSum(mat: Array<IntArray>): Int {
        var result = 0
        val n = mat.size
        for (i in 0 until n) {
            if ((i != n - i - 1)) {
                result += mat[i][n - i - 1]
            }
            result += mat[i][i]
        }
        return result
    }
}

fun main() {
    val sol = `1572 Matrix Diagonal Sum`()
    val matrix = arrayOf(
        intArrayOf(1, 2, 3),
        intArrayOf(4, 5, 6),
        intArrayOf(7, 8, 9)
    )
    val result = sol.diagonalSum(matrix)
    assert(result == 25) { "Test case failed: Expected 25 but got $result" }
    println("Test case passed")
}
