# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:
#
# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
#
# Output: 4
#
# Explanation:
#
# The longest valid subsequence is [1, 2, 3, 4].
#
# Example 2:
#
# Input: nums = [1,2,1,1,2,1,2]
#
# Output: 6
#
# Explanation:
#
# The longest valid subsequence is [1, 2, 1, 2, 1, 2].
#
# Example 3:
#
# Input: nums = [1,3]
#
# Output: 2
#
# Explanation:
#
# The longest valid subsequence is [1, 3].
#
#
#
# Constraints:
#
# 2 <= nums.length <= 2 * 105
# 1 <= nums[i] <= 107
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        countEven = 0
        countOdd = 0
        N = len(nums)
        for i in range(N):
            if nums[i] % 2 == 0:
                countEven += 1
            else:
                countOdd += 1

        # count start even
        needEven = True
        count1 = 0
        for i in range(N):
            if nums[i] % 2 == 0 and needEven:
                needEven = False
                count1 += 1
            elif nums[i] % 2 == 1 and not needEven:
                needEven = True
                count1 += 1

        needOdd = True
        count2 = 0
        for i in range(N):
            if nums[i] % 2 == 1 and needOdd:
                needOdd = False
                count2 += 1
            elif nums[i] % 2 == 0 and not needOdd:
                needOdd = True
                count2 += 1

        return max(count1, count2, countEven, countOdd)


sol = Solution()
assert sol.maximumLength([1, 2, 3, 4]) == 4
assert sol.maximumLength([1, 2, 1, 1, 2, 1, 2]) == 6
