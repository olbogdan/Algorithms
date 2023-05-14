package leetcode.hard

import kotlin.math.max

/*You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.



Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106*/
class `1799 Maximize Score After N Operations` {

    fun maxScore(nums: IntArray): Int {
        val memo = mutableMapOf<Int, Int>()
        val n = nums.size

        fun dp(mask: Int, operation: Int): Int {
            if (mask in memo) {
                return memo[mask]!!
            }

            for (i in 0 until n) {
                for (j in i + 1 until n) {
                    // mask 1110000 & curI 001000 -> 0010000 True
                    // mask 1110000 & curJ 000010 -> 0000000 False
                    if (mask and (1 shl i) != 0 || mask and (1 shl j) != 0) {
                        continue
                    }

                    val newMask = mask or (1 shl i) or (1 shl j)
                    var takeCurrent = operation * gcd(nums[i], nums[j])
                    takeCurrent += dp(newMask, operation + 1)
                    memo[mask] = max(takeCurrent, memo.getOrDefault(mask, 0))
                }
            }

            return memo.getOrDefault(mask, 0)
        }

        return dp(0, 1)
    }

    private fun gcd(a: Int, b: Int): Int {
        return if (b == 0) a else gcd(b, a % b)
    }
}

fun main() {
    val solution = `1799 Maximize Score After N Operations`()
    
    val nums = intArrayOf(2, 3, 4, 6)
    val maxScore = solution.maxScore(nums)
    println("Max score: $maxScore")
}
