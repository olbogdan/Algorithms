# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#
#
# Example 1:
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:
#
# Input: nums = [1,5]
# Output: 10
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dp(L, R):
            if L > R:
                return 0
            if (L, R) in cache:
                return cache[(L, R)]

            cache[(L, R)] = 0
            # R inclusive
            for i in range(L, R + 1):
                # calculate the i as an last element
                # this mean it will be 1 + 55 + 1
                count = nums[L - 1] * nums[i] * nums[R + 1]
                count += dp(L, i - 1) + dp(i + 1, R)
                cache[(L, R)] = max(cache[(L, R)], count)
            return cache[(L, R)]

        # [1] [34(L), 55, 99(R)] [1]
        return dp(1, len(nums) - 2)


sol = Solution()
assert sol.maxCoins([3,1,5,8]) == 167
