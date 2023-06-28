package leetcode.medium
/*You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.



Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.


Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes*/
import java.util.*
import kotlin.collections.HashMap

class `1514 Path with Maximum Probability` {
    fun maxProbability(n: Int, edges: Array<IntArray>, succProb: DoubleArray, start: Int, end: Int): Double {
        val adj = HashMap<Int, MutableList<Pair<Int, Double>>>()
        for (i in edges.indices) {
            val (a, b) = edges[i]
            adj.getOrPut(a) { mutableListOf() }.add(Pair(b, succProb[i]))
            adj.getOrPut(b) { mutableListOf() }.add(Pair(a, succProb[i]))
        }

        val visited = mutableSetOf<Int>()
        val pq = PriorityQueue<Pair<Double, Int>>(compareBy { it.first })
        pq.offer(Pair(-1.0, start))

        while (pq.isNotEmpty()) {
            val (prob, node) = pq.poll()
            visited.add(node)
            if (node == end) {
                return prob * -1
            }
            adj[node]?.let { neiList ->
                for ((nei, neiProb) in neiList) {
                    if (nei !in visited) {
                        pq.offer(Pair(neiProb * prob, nei))
                    }
                }
            }
        }
        return 0.0
    }
}

fun main() {
    val sol = `1514 Path with Maximum Probability`()
    val n = 3
    val edges = arrayOf(intArrayOf(0, 1), intArrayOf(1, 2), intArrayOf(0, 2))
    val succProb = doubleArrayOf(0.5, 0.5, 0.2)
    val start = 0
    val end = 2
    val result = sol.maxProbability(n, edges, succProb, start, end)
    print(result)
    require(0.25 == result)
}