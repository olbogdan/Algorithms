package leetcode.medium
/*Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109*/


class `18 4Sum` {
    fun fourSum(nums: IntArray, target: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        nums.sort()
        val n = nums.size

        for (i1 in 0 until n - 3) {
            //skip duplicates
            if (i1 >= 1 && nums[i1] == nums[i1 - 1]) {
                continue
            }

            for (i2 in i1 + 1 until n - 2) {
                if (i2 >= i1 + 2 && nums[i2] == nums[i2 - 1]) {
                    continue
                }

                // [L1, 2, 3, R4]
                // solve 2 sum sorted problem
                var L = i2 + 1
                var R = n - 1
                while (L < R) {
                    val sum = nums[i1].toLong() + nums[i2].toLong() + nums[L].toLong() +nums[R].toLong()
                    when {
                        sum < target -> L++
                        sum > target -> R--
                        else -> {
                            result.add(listOf(nums[i1], nums[i2], nums[L], nums[R]))
                            L++
                            R--

                            // skip duplicates
                            while (L < R && nums[L] == nums[L - 1]) {
                                L++
                            }
                        }
                    }
                }
            }
        }
        return result.toList()
    }
}

fun main() {
    val solution = `18 4Sum`()

    // Test case 1
    val nums1 = intArrayOf(1000000000, 1000000000, 1000000000, 1000000000)
    val target1 = -294967296
    val expected1 = emptyList<List<Int>>()
    val result1 = solution.fourSum(nums1, target1)
    assert(result1 == expected1) { "Test case 1 failed" }

    // Test case 2
    val nums2 = intArrayOf(1, 0, -1, 0, -2, 2)
    val target2 = 0
    val expected2 = listOf(listOf(-2, -1, 1, 2), listOf(-2, 0, 0, 2), listOf(-1, 0, 0, 1))
    val result2 = solution.fourSum(nums2, target2)
    assert(result2 == expected2) { "Test case 2 failed" }

    println("All tests passed")
}