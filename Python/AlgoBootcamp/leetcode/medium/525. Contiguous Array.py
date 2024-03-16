# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # [0, 1, 1, 0, 0]
        # [-1, 0, 1, 0, -1]
        memo = {}
        result = 0
        prev = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                prev += 1
            else:
                prev -= 1

            if prev == 0:
                result = i + 1
            elif prev in memo:
                result = max(result, i - memo[prev])
            else:
                memo[prev] = i
        return result


sol = Solution()
assert sol.findMaxLength([0, 1]) == 2
assert sol.findMaxLength([0, 1, 0]) == 2
assert sol.findMaxLength([0, 1, 1, 0, 0]) == 4
