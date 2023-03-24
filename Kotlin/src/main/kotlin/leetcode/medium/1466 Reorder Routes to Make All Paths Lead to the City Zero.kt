package leetcode.medium

class `1466 Reorder Routes to Make All Paths Lead to the City Zero` {
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val adj = mutableMapOf<Int, MutableList<Int>>() // original direction
        val directions = mutableSetOf<Pair<Int, Int>>()
        for (connection in connections) {
            adj.getOrPut(connection[0]) { mutableListOf() }.add(connection[1])
            adj.getOrPut(connection[1]) { mutableListOf() }.add(connection[0])
            directions.add(Pair(connection[0], connection[1]))
        }
        val visited = mutableSetOf(0)
        var result = 0

        fun dfs(node: Int) {
            visited.add(node)
            for (nei in adj.getOrDefault(node, mutableListOf())) {
                if (nei in visited) {
                    continue
                }
                // wrong direction, should be reversed
                if (Pair(node, nei) in directions) {
                    result++
                }
                dfs(nei)
            }
        }

        dfs(0)
        return result
    }
}

fun main() {
    val solution = `1466 Reorder Routes to Make All Paths Lead to the City Zero`()
    val connections1 = arrayOf(
        intArrayOf(0, 1),
        intArrayOf(1, 3),
        intArrayOf(2, 3),
        intArrayOf(4, 0),
        intArrayOf(4, 5)
    )
    assert(solution.minReorder(6, connections1) == 3)

    val connections2 = arrayOf(
        intArrayOf(1, 0),
        intArrayOf(2, 0)
    )
    assert(solution.minReorder(3, connections2) == 0)
}