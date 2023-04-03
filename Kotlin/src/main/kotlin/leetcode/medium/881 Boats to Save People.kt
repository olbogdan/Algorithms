package leetcode.medium

import kotlin.test.assertEquals


class `881 Boats to Save People`  {
    fun numRescueBoats(people: IntArray, limit: Int): Int {
        val sortedPeople = people.sortedArray()
        var left = 0
        var right = sortedPeople.size - 1
        var result = 0

        while (left <= right) {
            result++
            if (sortedPeople[right] + sortedPeople[left] <= limit) {
                right--
                left++
            } else {
                right--
            }
        }

        return result
    }
}

fun main() {
    val solution = `881 Boats to Save People`()

    val people = intArrayOf(1, 2, 2, 3)
    val limit = 3
    val expected = 3
    val actual = solution.numRescueBoats(people, limit)

    assertEquals(expected, actual)
}


