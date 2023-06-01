package leetcode.medium
/*Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1*/
import java.util.*

class `1091 Shortest Path in Binary Matrix` {
    fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
        val queue: Queue<Triple<Int, Int, Int>> = LinkedList() // row, col, len
        queue.offer(Triple(0, 0, 1))
        val visited = mutableSetOf<Pair<Int, Int>>()
        visited.add(0 to 0)

        val N = grid.size
        val end = N - 1 to N - 1
        val directions = arrayOf(
            0 to 1, 0 to -1, 1 to 0, -1 to 0,
            -1 to -1, 1 to 1, -1 to 1, 1 to -1
        )
        while (queue.isNotEmpty()) {
            val (r, c, length) = queue.poll()
            if (r < 0 || c < 0 || r >= N || c >= N || grid[r][c] == 1)
                continue
            if (r to c == end)
                return length
            for ((rOffset, cOffset) in directions) {
                val row = r + rOffset
                val col = c + cOffset
                if ((row to col) !in visited) {
                    queue.offer(Triple(row, col, length + 1))
                    visited.add(row to col)
                }
            }
        }

        return -1
    }
}
