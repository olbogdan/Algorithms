package leetcode.medium
/*Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20*/


class `59 Spiral Matrix II` {
    fun generateMatrix(n: Int): Array<IntArray> {
        val result = Array(n) { IntArray(n) }
        var iterI = 1
        val topI = n * n

        var offset = 0
        while (iterI <= topI) {
            for (i in offset until n - offset) {
                result[offset][i] = iterI
                iterI++
            }
            if (iterI > topI) break
            for (i in offset + 1 until n - offset) {
                result[i][n - offset - 1] = iterI
                iterI++
            }

            for (i in n - offset - 2 downTo offset) {
                result[n - offset - 1][i] = iterI
                iterI++
            }

            for (i in n - offset - 2 downTo offset + 1) {
                result[i][offset] = iterI
                iterI++
            }

            offset++
        }
        return result
    }
}
