# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
#
# A subarray is a contiguous part of the array.
#
#
#
# Example 1:
#
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:
#
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.numSubarraysWithLessOrEqualsSum(nums, goal) - self.numSubarraysWithLessOrEqualsSum(nums, goal - 1)

    def numSubarraysWithLessOrEqualsSum(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0
        l = 0
        curSum = 0
        result = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum > goal:
                curSum -= nums[l]
                l += 1
            result += (r - l + 1)
        return result


sol = Solution()
assert sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4
assert sol.numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15
