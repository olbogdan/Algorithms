# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
#
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = M = 0
        R = len(nums)-1
        while L <= R:
            if nums[L] == 0:
                # [0,0,1,0,0]
                nums[L], nums[M] = nums[M], nums[L]
                M += 1
                L += 1
            elif nums[L] == 1:
                # keep M on found 1n, iterate L
                L += 1
            elif nums[L] == 2:
                # move 2 to max right
                nums[L], nums[R] = nums[R], nums[L]
                R -= 1


sol = Solution()
arr = [2,0,2,1,1,0]
sol.sortColors(arr)
assert arr == [0,0,1,1,2,2]


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i1, i2):
            nums[i1], nums[i2] = nums[i2], nums[i1]

        N = len(nums)
        l = 0
        r = N - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                i += 1
                l += 1
            if nums[i] == 2:
                swap(r, i)
                r -= 1
            else:
                i += 1


sol = Solution2()
arr = [2, 0, 1]
sol.sortColors(arr)