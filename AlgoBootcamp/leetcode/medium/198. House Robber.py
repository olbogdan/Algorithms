# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums) -> int:

    memo = {}

    def dp(i):
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        val = max(nums[i] + dp( i +2), dp( i +1))
        memo[i] = val
        return val

    return dp(0)

assert rob([1,2,3,1]) == 4
assert rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]) == 3365