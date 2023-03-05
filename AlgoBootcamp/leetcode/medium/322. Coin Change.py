# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# #DP
from functools import cache
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)] * (amount+1) # [inf(0), inf(1), inf(2)] for amount 2
        dp[0] = 0
        coins.sort()
        for i in range(len(dp)):
            for c in coins:
                if c > i:
                    break
                prevAmount = dp[i - c]
                dp[i] = min(dp[i], prevAmount+1)
        if dp[amount] == float(inf):
            return -1
        return dp[amount]


sol = Solution()
assert sol.coinChange([1, 2, 5], 11) == 3
assert sol.coinChange([1], 11) == 11
assert sol.coinChange([100], 11) == -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i, am):
            if i == len(coins) or am < 0:
                return float(inf)
            if am == 0:
                return 0

            return min(1 + dp(i, am - coins[i]), dp(i + 1, am))

        r = dp(0, amount)
        if r == float(inf):
            return -1
        return r