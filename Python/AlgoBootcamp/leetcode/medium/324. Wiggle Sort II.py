# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# You may assume the input array always has a valid answer.
#
#
#
# Example 1:
#
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# Example 2:
#
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.
#
#
# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]):

        # sorted copy of original array
        array = sorted(nums)

        # take the bigest elements and insert them into odd positions
        for i in range(1, len(nums), 2):
            nums[i] = array.pop()

        # insert remaining elements into even positions
        for i in range(0, len(nums), 2):
            nums[i] = array.pop()
        return nums


sol = Solution()
arr = sol.wiggleSort([1,5,1,1,6,4])
assert arr == [1,6,1,5,1,4]
arr = sol.wiggleSort([4, 5, 5, 6])
assert arr == [5,6,4,5]
