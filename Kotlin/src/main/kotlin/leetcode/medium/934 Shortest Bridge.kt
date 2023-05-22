package leetcode.medium
/*You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.*/
import leetcode.hard.`41 First Missing Positive`
import java.util.*
import kotlin.test.assertEquals
// O(n^2)
class `934 Shortest Bridge` {
    fun shortestBridge(grid: Array<IntArray>): Int {
        val firstLand = findLand(grid)
        val (watterFront, visitedLand) = findWatterFront(grid, firstLand)
        return findClosestLand(grid, watterFront, visitedLand)
    }

    private fun findClosestLand(
        grid: Array<IntArray>,
        watterFront: Set<Pair<Int, Int>>,
        visited: MutableSet<Pair<Int, Int>>
    ): Int {
        val q: Queue<Pair<Int, Int>> = LinkedList(watterFront)
        var distance = 0
        while (q.isNotEmpty()) {
            val N = q.size
            repeat(N) {
                val (r, c) = q.poll()
                if ((r to c) in visited || minOf(r, c) < 0 || r >= grid.size || c >= grid[0].size) {
                    return@repeat
                }
                visited.add(r to c)
                if (grid[r][c] == 1) {
                    return distance
                }
                q.offer(r - 1 to c)
                q.offer(r + 1 to c)
                q.offer(r to c - 1)
                q.offer(r to c + 1)
            }
            distance++
        }
        return Int.MAX_VALUE
    }

    private fun findWatterFront(
        grid: Array<IntArray>,
        land: IntArray
    ): Pair<Set<Pair<Int, Int>>, MutableSet<Pair<Int, Int>>> {
        val watter = mutableSetOf<Pair<Int, Int>>()
        val visitedLand = mutableSetOf<Pair<Int, Int>>()

        fun dfs(r: Int, c: Int) {
            if (minOf(r, c) < 0 || r >= grid.size || c >= grid[0].size) {
                return
            }
            if ((r to c) in visitedLand || (r to c) in watter) {
                return
            }

            if (grid[r][c] == 0) {
                watter += r to c
            } else {
                visitedLand += r to c
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
            }
        }

        dfs(land[0], land[1])
        return watter to visitedLand
    }

    private fun findLand(grid: Array<IntArray>): IntArray {
        for (r in grid.indices) {
            for (c in grid[0].indices) {
                if (grid[r][c] == 1) {
                    return intArrayOf(r, c)
                }
            }
        }
        throw Exception("Grid has no land")
    }
}

fun main() {
    val sol = `934 Shortest Bridge`()
    var res = sol.shortestBridge(
        arrayOf(
            intArrayOf(1, 1, 1, 1, 1),
            intArrayOf(1, 0, 0, 0, 1),
            intArrayOf(1, 0, 1, 0, 1),
            intArrayOf(1, 0, 0, 0, 1),
            intArrayOf(1, 1, 1, 1, 1)
        )
    )
    assertEquals(res, 1)
    res = sol.shortestBridge(
        arrayOf(
            intArrayOf(0, 1, 0),
            intArrayOf(0, 0, 0),
            intArrayOf(0, 0, 1)
        )
    )

    assertEquals(res, 2)
}

