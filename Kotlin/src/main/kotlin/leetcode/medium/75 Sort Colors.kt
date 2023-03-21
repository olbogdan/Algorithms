package leetcode.medium
/*Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?*/


class SortColors {
    fun sortColors(nums: IntArray) {
        var left = 0
        var right = nums.size - 1
        var i = 0

        while (i <= right) {
            when {
                nums[i] == 0 -> {
                    nums[i] = nums[left]
                    nums[left] = 0
                    left++
                    i++
                }
                nums[i] == 2 -> {
                    nums[i] = nums[right]
                    nums[right] = 2
                    right--
                }
                else -> {
                    i++
                }
            }
        }
    }
}

class SortColors2 {
    fun sortColors(nums: IntArray) {
        var l = 0
        var r = nums.lastIndex
        var i = 0

        while (i <= r) {
            when (nums[i]) {
                0 -> nums[i] = nums[l].also { nums[l++] = 0 }
                2 -> nums[i] = nums[r].also { nums[r--] = 2; i-- }
            }
            i++
        }
    }
}