# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#
#
#
# Example 1:
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# Example 2:
#
# Input: num = 0
# Output: 0
#
#
# Constraints:
#
# 0 <= num <= 231 - 1
#
#
# Follow up: Could you do it without any loop/recursion in O(1) runtime?


class Solution:
    def addDigits(self, num: int) -> int:
        # 0 - 0
        # 1 - 1
        # 9 - 9
        # 10 - 1
        # 11 - 2
        # 18 - 9
        # 19 - 1
        # 20 - 2
        # 21 - 3
        if num == 0:
            return 0

        mod = num % 9
        if mod == 0:
            return 9
        else:
            return mod


sol = Solution()
assert sol.addDigits(38) == 2
assert sol.addDigits(0) == 0
