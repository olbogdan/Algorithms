package leetcode.medium
/*You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.



Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.*/
class `1020 Number of Enclaves` {
    fun numEnclaves(grid: Array<IntArray>): Int {
        val ROWS = grid.size
        val COLS = grid[0].size

        // let's modify the grid instead of visited set
        // visited = set()

        val directions = listOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))
        fun dfs(r: Int, c: Int): Int {
            if (r == -1 || r == ROWS || c == -1 || c == COLS || grid[r][c] != 1) {
                return 0
            }
            var res = 1
            // mark as visited by setting grid -1
            grid[r][c] = -1
            for ((dirR, dirC) in directions) {
                res += dfs(r + dirR, c + dirC)
            }
            return res
        }

        var lend = 0
        var borderLend = 0
        for (r in 0 until ROWS) {
            for (c in 0 until COLS) {
                if ((r == 0 || c == 0 || r == ROWS - 1 || c == COLS - 1) && grid[r][c] == 1) {
                    borderLend += dfs(r, c)
                }
                // count all 1 and -1 lands
                if (grid[r][c] != 0) {
                    lend += 1
                }
            }
        }
        return lend - borderLend
    }
}
