# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
#
#
# Example 1:
#
# Input: n = 16
# Output: true
# Example 2:
#
# Input: n = 5
# Output: false
# Example 3:
#
# Input: n = 1
# Output: true
#
#
# Constraints:
#
# -231 <= n <= 231 - 1
#
#
# Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        def power(number) -> bool:
            if number == n:
                return True
            elif number > n:
                return False
            return power(number * 4)

        return power(4)


sol = Solution()
res = sol.isPowerOfFour(64)
assert res is True
