package leetcode.hard
/*You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.



Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105
*/
class `2328 Number of Increasing Paths in a Grid` {

    fun countPaths(grid: Array<IntArray>): Int {
        val mod = 1_000_000_007
        val ROWS = grid.size
        val COLS = grid[0].size
        val memo = mutableMapOf<Pair<Int, Int>, Int>()
        fun dp(r: Int, c: Int, prev: Int, visited: MutableSet<Pair<Int, Int>>): Int {
            if (minOf(r, c) < 0 || r >= ROWS || c >= COLS) {
                return 0
            }
            if (grid[r][c] <= prev || visited.contains(r to c)) {
                return 0
            }
            memo[r to c]?.let { return it }
            visited.add(r to c)
            val curValue = grid[r][c]
            var result = 1
            // go 4 direction dfs to sum with result
            result = (result + dp(r - 1, c, curValue, visited)) % mod
            result = (result + dp(r, c - 1, curValue, visited)) % mod
            result = (result + dp(r + 1, c, curValue, visited)) % mod
            result = (result + dp(r, c + 1, curValue, visited)) % mod
            visited.remove(r to c)
            memo[r to c] = result
            return result
        }

        var result = 0
        for (r in 0 until ROWS) {
            for (c in 0 until COLS) {
                result = (result + dp(r, c, Int.MIN_VALUE, mutableSetOf())) % mod
            }
        }
        return result
    }
}

fun main() {
    val sol = `2328 Number of Increasing Paths in a Grid`()
    val grid1 = arrayOf(
        intArrayOf(1, 2)
    )
    require(sol.countPaths(grid1) == 3)

    val grid2 = arrayOf(
        intArrayOf(1, 1),
        intArrayOf(3, 4)
    )
    require(sol.countPaths(grid2) == 8)
}
