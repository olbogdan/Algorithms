package leetcode.easy

import kotlin.test.assertEquals

/*Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.*/
class NumArray(nums: IntArray) {
    private val prefixes = IntArray(nums.size)

    init {
        prefixes[0] = nums[0]
        for (i in 1 until nums.size) {
            prefixes[i] = prefixes[i-1] + nums[i]
        }
    }

    fun sumRange(left: Int, right: Int): Int {
        val rightSum = prefixes[right]
        val leftSum = if (left > 0) prefixes[left-1] else 0
        return rightSum - leftSum
    }
}

fun main() {
    val nums = intArrayOf(-2, 0, 3, -5, 2, -1)
    val numArray = NumArray(nums)

    // Test case 1
    val result1 = numArray.sumRange(0, 2)
    assertEquals(result1, 1)

    // Test case 2
    val result2 = numArray.sumRange(2, 5)
    assertEquals(result2, -1)
}