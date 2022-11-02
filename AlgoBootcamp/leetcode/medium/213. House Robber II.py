# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
# two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of
# money you can rob tonight without alerting the police.
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 3
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}

        def dfs(k, end):
            if k > end:
                return 0
            if k in memo:
                return memo[k]
            curVal = nums[k]
            value = max(curVal + dfs(k + 2, end), dfs(k + 1, end))
            memo[k] = value
            return value

        first = dfs(0, len(nums) - 2)
        memo.clear()
        second = dfs(1, len(nums) - 1)
        return max(first, second)


sol = Solution()
assert sol.rob([2,3,2]) == 3
assert sol.rob([1,2,3,1]) == 4
assert sol.rob([0]) == 0
assert sol.rob([1]) == 1
