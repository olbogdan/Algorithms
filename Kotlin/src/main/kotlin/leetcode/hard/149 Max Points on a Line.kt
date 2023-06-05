package leetcode.hard

import java.util.*

class `149 Max Points on a Line`  {
    fun maxPoints(points: Array<IntArray>): Int {
        // use formula (y1 - y2) / (x1 - x2)
        // iterate n^2 loop to check connection of each point with others
        // return max
        val N = points.size
        var res = 1
        for (i in 0 until N) {
            val (x1, y1) = points[i]
            val count = HashMap<Double, Int>()
            for (j in i + 1 until N) {
                val (x2, y2) = points[j]
                var slope = N + 1.toDouble()
                if (x1 != x2) {
                    if (y1 == y2) {
                        slope = 0.0
                    } else {
                        slope = (y1 - y2).toDouble() / (x1 - x2).toDouble()
                    }
                }
                count[slope] = count.getOrDefault(slope, 0) + 1
                res = maxOf(res, count[slope]!! + 1)
            }
        }
        return res
    }
}

fun main() {
    val solution = `149 Max Points on a Line` ()
    require(solution.maxPoints(arrayOf(intArrayOf(1,1), intArrayOf(2,2), intArrayOf(3,3))) == 3)
    require(solution.maxPoints(arrayOf(intArrayOf(2,3), intArrayOf(3,3), intArrayOf(-5, 3))) == 3)
    require(solution.maxPoints(arrayOf(intArrayOf(1,1), intArrayOf(3,2), intArrayOf(5,3), intArrayOf(4,1), intArrayOf(2,3), intArrayOf(1,4))) == 4)
}