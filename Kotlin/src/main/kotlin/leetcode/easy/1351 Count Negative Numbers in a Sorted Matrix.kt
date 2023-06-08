package leetcode.easy
/*Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100


Follow up: Could you find an O(n + m) solution?*/
class `1351 Count Negative Numbers in a Sorted Matrix` {
    fun countNegatives(grid: Array<IntArray>): Int {
        val ROWS = grid.size
        val COLS = grid[0].size

        var curRow = ROWS - 1
        var curCol = 0

        var result = 0
        while (curCol < COLS && curRow >= 0) {
            if (grid[curRow][curCol] >= 0) {
                curCol++
                continue
            }
            result += COLS - curCol
            curRow--
        }
        return result
    }
}
