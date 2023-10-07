# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
#
# Return the maximum product you can get.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
#
# Constraints:
#
# 2 <= n <= 58


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        reminder = n % 3
        reps = n // 3
        if reminder == 0:
            return int(math.pow(3, reps))
        else:
            # rem is 1 or 2
            if reminder == 2:
                return int(math.pow(3, reps) * 2)
            else:
                return int(math.pow(3, (reps - 1)) * 4)