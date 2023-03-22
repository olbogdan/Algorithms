package leetcode.medium

class MinScoreOfPathTwo {
    fun minScore(n: Int, roads: Array<IntArray>): Int {
        val adj = mutableMapOf<Int, MutableSet<Pair<Int, Int>>>()
        for ((a, b, dist) in roads) {
            adj[a] = (adj[a] ?: mutableSetOf()).apply { add(Pair(b, dist)) }
            adj[b] = (adj[b] ?: mutableSetOf()).apply { add(Pair(a, dist)) }
        }

        val visited = mutableSetOf<Int>()
        var result = Int.MAX_VALUE

        fun dfs(node: Int) {
            if (node in visited) {
                return
            }
            visited.add(node)
            if (adj[node] != null) {
                for ((nei, dist) in adj[node]!!) {
                    result = minOf(result, dist)
                    dfs(nei)
                }
            }
        }
        dfs(n)
        return result
    }
}