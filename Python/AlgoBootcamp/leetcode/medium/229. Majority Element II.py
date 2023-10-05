# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
#
# Input: nums = [1]
# Output: [1]
# Example 3:
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow up: Could you solve the problem in linear time and in O(1) space?
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        third = len(nums) // 3
        result = []
        for k, v in count.items():
            if v > third:
                result.append(k)
            if len(result) == 2:
                break
        return result
    