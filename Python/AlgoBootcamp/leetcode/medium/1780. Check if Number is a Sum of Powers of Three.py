# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
#
# An integer y is a power of three if there exists an integer x such that y == 3x.
#
#
#
# Example 1:
#
# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32
# Example 2:
#
# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34
# Example 3:
#
# Input: n = 21
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 107


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, runSum):
            if runSum == n:
                return True
            if runSum > n or 3**i > n:
                return False
            if backtrack(i+1, runSum + 3**i):
                return True
            else:
                return backtrack(i+1, runSum)
        return backtrack(0, 0)


sol = Solution()
assert sol.checkPowersOfThree(12) is True
assert sol.checkPowersOfThree(91) is True
assert sol.checkPowersOfThree(21) is False
