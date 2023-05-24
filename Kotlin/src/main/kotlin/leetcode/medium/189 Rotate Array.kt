package leetcode.medium
/*Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?*/

class `189 Rotate Array`  {
    fun rotate(nums: IntArray, k: Int): Unit {
        val N = nums.size
        // rotate array
        helper(nums, 0, N - 1)
        val kModN = k % N
        helper(nums, 0, kModN - 1)
        helper(nums, kModN, N - 1)
    }

    private fun helper(nums: IntArray, l: Int, r: Int): Unit {
        var left = l
        var right = r
        while (left < right) {
            val temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left++
            right--
        }
    }
}

fun main(args: Array<String>) {
    val nums = intArrayOf(1, 2, 3, 4, 5, 6, 7)
    `189 Rotate Array` ().rotate(nums, 3)
    assert(nums contentEquals intArrayOf(5, 6, 7, 1, 2, 3, 4))

    val nums2 = intArrayOf(-1, -100, 3, 99)
    `189 Rotate Array` ().rotate(nums2, 2)
    assert(nums2 contentEquals intArrayOf(3, 99, -1, -100))
}
