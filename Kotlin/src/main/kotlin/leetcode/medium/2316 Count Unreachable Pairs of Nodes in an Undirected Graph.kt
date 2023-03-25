package leetcode.medium

import java.util.*

class `2316 Count Unreachable Pairs of Nodes in an Undirected Graph` {
    fun countPairs(n: Int, edges: List<List<Int>>): Int {
        var n = n
        val adj = hashMapOf<Int, MutableList<Int>>()
        for (edge in edges) {
            val a = edge[0]
            val b = edge[1]
            adj.getOrPut(a, { mutableListOf() }).add(b)
            adj.getOrPut(b, { mutableListOf() }).add(a)
        }

        val components = mutableListOf<Int>()
        val visited = mutableSetOf<Int>()

        var currentNodeCount = 0

        fun dfs(node: Int) {
            if (adj[node] != null) {
                for (nei in adj[node]!!) {
                    if (nei in visited) continue
                    currentNodeCount++
                    visited.add(nei)
                    dfs(nei)
                }
            }
        }

        for (i in 0 until n) {
            if (i in visited) continue
            currentNodeCount = 1
            visited.add(i)
            dfs(i)
            components.add(currentNodeCount)
        }

        var res = 0
        for (c in components) {
            res += c * (n - c)
            n -= c
        }
        return res
    }
}

fun main() {
    val sol = `2316 Count Unreachable Pairs of Nodes in an Undirected Graph`()
    var res = sol.countPairs(3, listOf(listOf(0, 1), listOf(0, 2), listOf(1, 2)))
    assert(res == 0)
    res = sol.countPairs(3, listOf(listOf(0, 1), listOf(2, 2)))
    assert(res == 2)
    res = sol.countPairs(12, emptyList())
    assert(res == 66)
}
