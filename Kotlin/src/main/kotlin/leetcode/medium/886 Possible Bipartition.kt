package leetcode.medium
import java.util.*

class `886 Possible Bipartition` {
    fun possibleBipartition(n: Int, dislikes: Array<IntArray>): Boolean {

        val adj = mutableMapOf<Int, MutableList<Int>>()
        for (dislike in dislikes) {
            val a = dislike[0]
            val b = dislike[1]
            adj.getOrPut(a, { mutableListOf() }).add(b)
            adj.getOrPut(b, { mutableListOf() }).add(a)
        }

        val whiteBlack = IntArray(n + 1) // 0 -> unvisited, 1 -> white, -1 -> black

        fun bfs(i: Int): Boolean {
            if (whiteBlack[i] != 0) return true

            val q: Queue<Int> = LinkedList()
            q.offer(i)

            whiteBlack[i] = -1
            while (q.isNotEmpty()) {
                val node = q.poll()
                val curColor = whiteBlack[node]
                adj[node]?.forEach { nei ->
                    if (whiteBlack[nei] == curColor) return false
                    else if (whiteBlack[nei] == 0) {
                        q.offer(nei)
                        whiteBlack[nei] = curColor * -1
                    }
                }
            }
            return true
        }

        for (i in 1..n) {
            if (!bfs(i)) return false
        }

        return true
    }
}

fun main() {
    val sol = `886 Possible Bipartition`()
    var res = sol.possibleBipartition(3, arrayOf(intArrayOf(1,2), intArrayOf(1,3), intArrayOf(2,3)))
    assert(!res)
    res = sol.possibleBipartition(3, arrayOf(intArrayOf(1,2), intArrayOf(1,3)))
    assert(res)
}
