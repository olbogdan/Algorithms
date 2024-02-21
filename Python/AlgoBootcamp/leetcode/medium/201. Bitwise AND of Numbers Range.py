# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
#
#
#
# Example 1:
#
# Input: left = 5, right = 7
# Output: 4
# Example 2:
#
# Input: left = 0, right = 0
# Output: 0
# Example 3:
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
# Constraints:
#
# 0 <= left <= right <= 231 - 1

# first loop:
#             101 >> 1 = 10
#             111 >> 1 = 11
#             cnt = 1
#
# Second loop:
#             10 >> 1 = 1
#             11 >> 1 = 1
#             cnt = 2
#
# Third loop:
#             1 == 1


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shft = 0
        while right != left:
            if left == 0:
                return 0
            shft += 1
            right = right >> 1
            left = left >> 1
        return right << shft


sol = Solution()
assert sol.rangeBitwiseAnd(5, 7) == 4
assert sol.rangeBitwiseAnd(0, 0) == 0
