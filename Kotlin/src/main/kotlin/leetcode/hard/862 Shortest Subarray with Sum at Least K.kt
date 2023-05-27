package leetcode.hard
/*Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3


Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
*/

import java.util.*

class `862 Shortest Subarray with Sum at Least K` {
    fun shortestSubarray(nums: IntArray, k: Int): Int {
        val N = nums.size
        val prefixes = LongArray(N + 1)
        for (i in 1..N) {
            prefixes[i] = nums[i - 1].toLong() + prefixes[i - 1]
        }

        var res = Int.MAX_VALUE
        val queue = LinkedList<Int>()
        for (i in prefixes.indices) {
            while (queue.isNotEmpty() && prefixes[i] - prefixes[queue.first] >= k) {
                res = minOf(res, i - queue.pollFirst())
            }

            while (queue.isNotEmpty() && prefixes[i] <= prefixes[queue.last]) {
                queue.pollLast()
            }

            queue.add(i)
        }
        return if (res == Int.MAX_VALUE) -1 else res
    }
}
