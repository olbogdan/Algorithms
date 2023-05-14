# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.
#
# In the ith operation (1-indexed), you will:
#
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.
#
# The function gcd(x, y) is the greatest common divisor of x and y.
#
#
#
# Example 1:
#
# Input: nums = [1,2]
# Output: 1
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 2)) = 1
# Example 2:
#
# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# Example 3:
#
# Input: nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
#
#
# Constraints:
#
# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 106
import math
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}
        N = len(nums)

        def dp(mask, operation):
            if mask in memo:
                return memo[mask]

            for i in range(N):
                for j in range(i + 1, N):
                    # mask 1110000 & curI 001000 -> 0010000 True
                    # mask 1110000 & curJ 000010 -> 0000000 False
                    if mask & (1 << i) or mask & (1 << j):
                        continue

                    newMask = mask | (1 << i) | (1 << j)
                    takeCurrent = operation * math.gcd(nums[i], nums[j])
                    takeCurrent += dp(newMask, operation + 1)
                    memo[mask] = max(takeCurrent, memo.get(mask, 0))

            return memo.get(mask, 0)

        return dp(0, 1)


sol = Solution()
sol.maxScore([1,2,3,4,5,6]) == 14
