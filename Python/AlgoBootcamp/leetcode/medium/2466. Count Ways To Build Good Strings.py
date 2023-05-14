# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
#
# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.
#
# A good string is a string constructed by the above process having a length between low and high (inclusive).
#
# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: low = 3, high = 3, zero = 1, one = 1
# Output: 8
# Explanation:
# One possible valid good string is "011".
# It can be constructed as follows: "" -> "0" -> "01" -> "011".
# All binary strings from "000" to "111" are good strings in this example.
# Example 2:
#
# Input: low = 2, high = 3, zero = 1, one = 2
# Output: 5
# Explanation: The good strings are "00", "11", "000", "110", and "011".
#
#
# Constraints:
#
# 1 <= low <= high <= 105
# 1 <= zero, one <= low
# #dp #stairs
from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        N = high
        memo = {0: 1}

        result = 0
        # [1, 0, 0, 0] 011
        for i in range(1, N + 1):
            memo[i] = (memo.get(i - zero, 0) + memo.get(i - one, 0)) % MOD

            if i >= low:
                result += memo[i]

        return result % MOD


sol = Solution()
assert sol.countGoodStrings(2, 3, 1, 2) == 5


class Solution1:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(length):

            if length > high:
                return 0
            count = 0
            if length >= low:
                count = 1
            count += dp(length + zero)
            count += dp(length + one)
            return count % MOD

        return dp(0)


sol = Solution1()
assert sol.countGoodStrings(2, 3, 1, 2) == 5


class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        N = high
        memo = {}
        memo[0] = 1

        result = 0
        # [1, 0, 0, 0] 011
        for i in range(1, N + 1):
            curr = 0
            # zeros
            zerosI = i - zero
            if zerosI in memo:
                curr = memo[zerosI]
            # ones
            onesI = i - one
            if onesI in memo:
                curr += memo[onesI]

            if curr != 0:
                memo[i] = curr

            if i >= low:
                result += curr
                result %= MOD

        return result


sol = Solution2()
assert sol.countGoodStrings(2, 3, 1, 2) == 5
