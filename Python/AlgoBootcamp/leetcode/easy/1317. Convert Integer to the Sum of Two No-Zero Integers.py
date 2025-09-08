# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
#
# Given an integer n, return a list of two integers [a, b] where:
#
# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# Example 2:
#
# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
#
#
# Constraints:
#
# 2 <= n <= 104
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n - 1
        while self.hasZero(a) or self.hasZero(b):
            a += 1
            b -= 1
        return [a, b]

    def hasZero(self, num: int) -> bool:
        while num > 0:
            if num % 10 == 0:
                return True
            num //= 10
        return False


sol = Solution()
assert sol.getNoZeroIntegers(2) == [1, 1]
assert sol.getNoZeroIntegers(11) == [2, 9]
