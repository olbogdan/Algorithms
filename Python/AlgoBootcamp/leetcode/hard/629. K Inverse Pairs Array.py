# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
#
# Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
# Example 2:
#
# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
#
#
# Constraints:
#
# 1 <= n <= 1000
# 0 <= k <= 1000
from functools import cache


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(n, k):
            if k == 0:
                # there is exactly one way to arrange the array (in increasing order)
                return 1
            if k < 0:
                # k in negative area - invalid
                return 0
            if n == 1:
                # can't create any (k) pairs if array has only 1 element
                return 0

            return (dp(n - 1, k) + dp(n, k - 1) - dp(n - 1, k - n)) % MOD

        return dp(n, k)


sol = Solution()
assert sol.kInversePairs(3, 1) == 2
