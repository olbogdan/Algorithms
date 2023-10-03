# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for n in nums:
            if count[n] > 0:
                result += count[n] - 1
                count[n] -= 1
        return result


assert Solution().numIdenticalPairs([1,2,3,1,1,3]) == 4


class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for n in nums:
            if count[n] > 1:
                result += count[n] * (count[n] - 1) // 2
                count[n] = 0
        return result
