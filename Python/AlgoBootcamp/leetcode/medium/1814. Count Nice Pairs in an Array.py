# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
#
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# Example 2:
#
# Input: nums = [13,10,35,24,76]
# Output: 4
from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def reverseNum(num: int) -> int:
            # 140
            stack = []
            for ch in str(num):
                stack.append(ch)
            while stack[-1] == 0 and len(stack) > 1:
                stack.pop()
            stack.reverse()
            return int("".join(stack))

        for i in range(len(nums)):
            rNum = reverseNum(nums[i])
            nums[i] = nums[i] - rNum

        counter = Counter(nums)
        result = 0
        for k, v in counter.items():
            if v > 0:
                result += v * (v - 1) // 2
        return result % MOD


sol = Solution()
assert sol.countNicePairs([13,10,35,24,76]) == 4
