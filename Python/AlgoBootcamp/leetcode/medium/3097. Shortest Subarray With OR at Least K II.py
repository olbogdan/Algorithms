# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty
# subarray
#  of nums, or return -1 if no special subarray exists.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], k = 2
#
# Output: 1
#
# Explanation:
#
# The subarray [3] has OR value of 3. Hence, we return 1.
#
# Example 2:
#
# Input: nums = [2,1,8], k = 10
#
# Output: 3
#
# Explanation:
#
# The subarray [2,1,8] has OR value of 11. Hence, we return 3.
#
# Example 3:
#
# Input: nums = [1,2], k = 0
#
# Output: 1
#
# Explanation:
#
# The subarray [1] has OR value of 1. Hence, we return 1.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 109
# 0 <= k <= 109
from cmath import inf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        mask = [0] * 32
        def updateByNumber(num, diff):
            for i in range(32):
                if num & (1 << i) > 0:
                    mask[i] += diff

        def getNumber():
            number = 0
            for i in range(32):
                if mask[i] > 0:
                    number = number | (1 << i)
            return number


        res = float(inf)
        l = 0
        for r in range(len(nums)):
            updateByNumber(nums[r], 1)
            cur = getNumber()
            while cur >= k:
                res = min(res, r - l + 1)
                updateByNumber(nums[l], -1)
                l += 1
                cur = getNumber()
        return res if res != float(inf) else -1


sol = Solution()
assert sol.minimumSubarrayLength([1,2,3], 2) == 1
assert sol.minimumSubarrayLength([2,1,8], 10) == 3
