# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
from math import inf


def coinChange(coins: [int], amount: int) -> int:
    memo = [float(inf)] * (amount + 1)
    memo[0] = 0
    coins.sort()

    for a in range(0, amount + 1):
        for c in coins:
            if c > a:
                break

            diff = a - c
            memo[a] = min(memo[a], 1 + memo[diff])

    if memo[-1] == float(inf):
        return -1
    else:
        return memo[-1]

assert coinChange([1, 2, 5], 11) == 3
assert coinChange([1], 11) == 11
assert coinChange([100], 11) == -1