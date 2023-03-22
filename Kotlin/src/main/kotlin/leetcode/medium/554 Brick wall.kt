package leetcode.medium

import kotlin.test.assertEquals

class BrickWall {
    fun leastBricks(wall: List<List<Int>>): Int {
        val withEnds = mutableMapOf(0 to 0)
        for (row in wall) {
            var curWith = 0
            for (w in row.dropLast(1)) {
                curWith += w
                withEnds[curWith] = 1 + withEnds.getOrDefault(curWith, 0)
            }
        }
        return wall.size - (withEnds.values.maxOrNull() ?: 0)
    }
}

fun main() {
    val sol = BrickWall()
    val res = sol.leastBricks(listOf(listOf(2, 3), listOf(2, 1,1,1)))
    assertEquals(res, 0)
}
