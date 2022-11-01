# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 40

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prevPrev = prev = 0
        for n in nums:
            temp = max(prev, prevPrev+n)
            prevPrev = prev
            prev = temp
        return prev


sol = Solution()
assert sol.rob([1,2,3,1]) == 4
assert sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]) == 3365


class Solution2:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(k):
            if k >= len(nums):
                return 0
            if k in memo:
                return memo[k]
            val = nums[k]
            cost = max(val + dfs(k+2), dfs(k+1))
            memo[k] = cost
            return cost
        return dfs(0)


sol = Solution2()
assert sol.rob([1,2,3,1]) == 4
assert sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]) == 3365
