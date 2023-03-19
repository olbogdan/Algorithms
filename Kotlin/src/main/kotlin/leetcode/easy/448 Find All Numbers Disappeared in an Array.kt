package leetcode.easy
/*Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.*/

import kotlin.math.abs
import kotlin.test.assertEquals

private class Solution2 {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        for (n in nums) {
            val i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        }

        val res = mutableListOf<Int>()
        for (i in nums.indices) {
            if (nums[i] > 0) {
                res.add(i + 1)
            }
        }
        return res
    }
}

fun main() {
    val sol = Solution2()

    val input = intArrayOf(4, 3, 2, 7, 8, 2, 3, 1)
    val output = sol.findDisappearedNumbers(input)
    assertEquals(output, listOf(5, 6))

    println("Test passed!")
}