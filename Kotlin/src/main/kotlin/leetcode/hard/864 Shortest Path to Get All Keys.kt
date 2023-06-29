package leetcode.hard
/*You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.



Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.*/
import java.util.*

class `864 Shortest Path to Get All Keys` {
    fun shortestPathAllKeys(grid: Array<String>): Int {
        val rows = grid.size
        val cols = grid[0].length
        var startX = 0
        var startY = 0
        var totalKeys = 0
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                if (grid[i][j] == '@') {
                    startX = i
                    startY = j
                } else if (grid[i][j].isLowerCase()) {
                    totalKeys++
                }
            }
        }

        var r = 0
        val visited = mutableSetOf(Triple(startX, startY, 0))
        val q: Queue<Triple<Int, Int, Int>> = LinkedList(listOf(Triple(startX, startY, 0)))

        while (q.isNotEmpty()) {
            val l = q.size
            for (i in 0 until l) {
                val (x, y, k) = q.poll()
                if (k == (1 shl totalKeys) - 1) {
                    return r
                }
                for ((dx, dy) in listOf(Pair(-1, 0), Pair(0, -1), Pair(0, 1), Pair(1, 0))) {
                    val newX = x + dx
                    val newY = y + dy
                    if (newX in 0 until rows && newY in 0 until cols && grid[newX][newY] != '#') {
                        var z = k
                        if (grid[newX][newY].isLowerCase()) {
                            z = z or (1 shl (grid[newX][newY].toInt() - 'a'.toInt()))
                        }
                        if (Triple(newX, newY, z) in visited || grid[newX][newY].isUpperCase() && z and (1 shl (grid[newX][newY].toInt() - 'A'.toInt())) == 0) {
                            continue
                        }
                        q.offer(Triple(newX, newY, z))
                        visited.add(Triple(newX, newY, z))
                    }
                }
            }
            r += 1
        }
        return -1
    }
}
