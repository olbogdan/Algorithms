# Given an array nums of integers, return how many of them contain an even number of digits.
#
#
#
# Example 1:
#
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:
#
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.
#
#
# Constraints:
#
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105
from math import log10
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if int(log10(nums[i]) + 1) % 2 == 0:
                res += 1
        return res


sol = Solution()
assert sol.findNumbers([12, 345, 2, 6, 7896]) == 2
assert sol.findNumbers([555, 901, 482, 1771]) == 1
