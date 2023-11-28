# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:
#
# A chess knight can move as indicated in the chess diagram below:
#
#
# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).
#
#
# Given an integer n, return how many distinct phone numbers of length n we can dial.
#
# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.
#
# As the answer may be very large, return the answer modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
# Example 2:
#
# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# Example 3:
#
# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.
#
#
# Constraints:
#
# 1 <= n <= 5000
from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {}
        adj[1] = [8, 6]
        adj[2] = [9, 7]
        adj[3] = [4, 8]
        adj[4] = [0, 3, 9]
        adj[5] = []
        adj[6] = [0, 1, 7]
        adj[7] = [2, 6]
        adj[8] = [1, 3]
        adj[9] = [2, 4]
        adj[0] = [4, 6]

        MOD = 10 ** 9 + 7

        cache = {}
        def dp(i, level):
            if level == 0:
                return 1
            elif (i, level) in cache:
                return cache[(i, level)]
            else:
                result = 0
                for nei in adj[i]:
                    result += dp(nei, level - 1)
                cache[(i, level)] = result
                return result

        result = 0
        for i in range(10):
            result += dp(i, n - 1)
            result %= MOD

        return result


sol = Solution()
assert sol.knightDialer(1) == 10
assert sol.knightDialer(2) == 20
