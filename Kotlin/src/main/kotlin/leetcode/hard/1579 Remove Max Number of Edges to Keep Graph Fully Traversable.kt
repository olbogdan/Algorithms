package leetcode.hard
/*Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.



Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.




Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.*/

class UF(n: Int) {
    var n = n
    var parents = IntArray(n + 1) { it }
    var rank = IntArray(n + 1) { 1 }

    fun find(i: Int): Int {
        if (parents[i] != i) {
            parents[i] = find(parents[i])
        }
        return parents[i]
    }

    // returns 0 if nodes are already connected, else 1
    fun union(i: Int, j: Int): Int {
        val iParent = find(i)
        val jParent = find(j)
        if (iParent == jParent) {
            return 0
        }
        if (rank[iParent] > rank[jParent]) {
            rank[iParent] += rank[jParent]
            parents[jParent] = iParent
        } else {
            rank[jParent] += rank[iParent]
            parents[iParent] = jParent
        }
        n -= 1
        return 1
    }

    fun isConnected(): Boolean {
        return n == 1
    }
}

class `1579 Remove Max Number of Edges to Keep Graph Fully Traversable` {
    fun maxNumEdgesToRemove(n: Int, edges: Array<IntArray>): Int {
        val alice = UF(n)
        val bob = UF(n)

        // let's count needed connections instead of removing them from edges
        var connections = 0

        // take all universal edges
        for ((type, u, v) in edges) {
            if (type == 3) {
                // adds connection if not added
                // increments connections if at least one new connection was added
                connections += (alice.union(u, v) or bob.union(u, v))
            }
        }

        // take any personal connection, if connection between edges does not exist yet
        for ((type, u, v) in edges) {
            when (type) {
                1 -> connections += alice.union(u, v)
                2 -> connections += bob.union(u, v)
            }
        }

        return if (alice.isConnected() && bob.isConnected())
            edges.size - connections
        else
            -1
    }
}

fun main() {
    val solution = `1579 Remove Max Number of Edges to Keep Graph Fully Traversable`()
    assert(solution.maxNumEdgesToRemove(4, arrayOf(
        intArrayOf(3, 1, 2),
        intArrayOf(3, 2, 3),
        intArrayOf(1, 1, 4),
        intArrayOf(2, 1, 4)
    )) == 2)

    assert(solution.maxNumEdgesToRemove(4, arrayOf(
        intArrayOf(3, 1, 2),
        intArrayOf(3, 2, 3),
        intArrayOf(1, 1, 4),
        intArrayOf(2, 1, 4),
        intArrayOf(1, 2, 4),
        intArrayOf(2, 2, 3)
    )) == 0)
}







