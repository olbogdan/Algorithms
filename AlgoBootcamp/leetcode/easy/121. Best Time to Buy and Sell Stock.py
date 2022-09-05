# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices: [int]) -> int:
    # [1, 2, 3, 4]
    # [1, 2, 1, 1]
    # [2, 3, 1, 3]
    # first pointer 0
    # second pointer 1
    # max = max p2 - p1 or max
    # if p2 < p1 -> p1 = p2

    if len(prices) <= 1:
        return 0

    slow = 0
    fast = 1
    maxValue = 0
    while fast < len(prices):
        if prices[fast] < prices[slow]:
            slow = fast
            fast += 1
            continue
        maxValue = max(maxValue, prices[fast] - prices[slow])
        fast += 1

    return maxValue


assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
assert maxProfit([]) == 0
assert maxProfit([1, 2]) == 1