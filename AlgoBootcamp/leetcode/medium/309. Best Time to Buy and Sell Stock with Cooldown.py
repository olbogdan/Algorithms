# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
#
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#
#
# Example 1:
#
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:
#
# Input: prices = [1]
# Output: 0
#
#
# Constraints:
#
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
from functools import cache
from typing import List


# [1, 5]
# balance = 0
# 1st step buy: 0-1 balance -1
# 2nd step sell: (-1) + 5 balance 4
# return balance
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, buy):
            if i >= len(prices):
                return 0

            if buy:
                # buy one, change the "buy" to the False to indicate we hold one stock
                b = dp(i + 1, False) - prices[i]
                # skip one, don't buy
                c = dp(i + 1, True)
                return max(b, c)
            else:
                # sell one, move pointer to 2 days cooldown
                b = dp(i + 2, True) + prices[i]
                # skip selling, don't sell
                c = dp(i + 1, False)
                return max(b, c)

        return dp(0, True)


sol = Solution()
assert sol.maxProfit([1,2,3,0,2]) == 3
assert sol.maxProfit([1]) == 0
