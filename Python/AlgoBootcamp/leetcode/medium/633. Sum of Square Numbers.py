# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
#
#
#
# Example 1:
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
#
# Input: c = 3
# Output: false
#
#
# Constraints:
#
# 0 <= c <= 231 - 1
from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l <= r:
            candidate = l * l + r * r
            if candidate < c:
                l += 1
            elif candidate > c:
                r -= 1
            else:
                return True
        return False


sol = Solution()
assert sol.judgeSquareSum(5)
assert not sol.judgeSquareSum(3)
