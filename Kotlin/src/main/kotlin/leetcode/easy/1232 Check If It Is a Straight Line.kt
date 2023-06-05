package leetcode.easy

import kotlin.math.abs

import kotlin.math.abs

class `1232 Check If It Is a Straight Line`  {
    fun checkStraightLine(coordinates: Array<IntArray>): Boolean {
        // slope = (y1 - y2) / (x1 - x2)
        if (coordinates.size == 2) {
            return true
        }

        val x1 = coordinates[0][0]
        val y1 = coordinates[0][1]
        val x2 = coordinates[1][0]
        val y2 = coordinates[1][1]
        var slope = Double.POSITIVE_INFINITY
        if (x1 != x2) {
            slope = (y1.toDouble() - y2.toDouble()) / (x1.toDouble() - x2.toDouble())
        }

        for (i in 2 until coordinates.size) {
            val x3 = coordinates[i][0]
            val y3 = coordinates[i][1]
            if (x1 == x2 && x1 == x3) {
                continue
            } else if (x1 == x2 || x1 == x3) {
                return false
            }

            val slope3 = (y1.toDouble() - y3.toDouble()) / (x1.toDouble() - x3.toDouble())
            if (slope != slope3) {
                return false
            }
        }
        return true
    }
}

fun main() {
    val solution = `1232 Check If It Is a Straight Line` ()
    assert(solution.checkStraightLine(arrayOf(intArrayOf(1,-8), intArrayOf(2,-3), intArrayOf(1,2))) == false)
    assert(solution.checkStraightLine(arrayOf(intArrayOf(1,2), intArrayOf(2,3), intArrayOf(3,4), intArrayOf(4,5), intArrayOf(5,6), intArrayOf(6,7))) == true)
    println("All tests passed!")
}
