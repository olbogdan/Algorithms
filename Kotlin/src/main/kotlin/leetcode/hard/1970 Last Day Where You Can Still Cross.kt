package leetcode.hard
/*There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.



Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.


Constraints:

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.*/


class `1970 Last Day Where You Can Still Cross` {

    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        var left = 1
        var right = row * col

        while (left < right) {
            val mid = right - (right - left) / 2
            if (isPossible(row, col, cells, mid)) {
                left = mid
            } else {
                right = mid - 1
            }
        }

        return left
    }

    private fun isPossible(row: Int, col: Int, cells: Array<IntArray>, day: Int): Boolean {
        val grid = Array(row) { IntArray(col) { 0 } }
        val queue = ArrayDeque<Pair<Int, Int>>()

        for (i in 0 until day) {
            val (r, c) = cells[i]
            grid[r - 1][c - 1] = 1
        }

        for (i in 0 until col) {
            if (grid[0][i] == 0) {
                queue.addLast(Pair(0, i))
                grid[0][i] = -1
            }
        }

        while (queue.isNotEmpty()) {
            val (r, c) = queue.removeFirst()
            if (r == row - 1) {
                return true
            }
            for ((dr, dc) in listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)) {
                val nr = r + dr
                val nc = c + dc
                if (nr in 0 until row && nc in 0 until col && grid[nr][nc] == 0) {
                    grid[nr][nc] = -1
                    queue.addLast(Pair(nr, nc))
                }
            }
        }

        return false
    }
}