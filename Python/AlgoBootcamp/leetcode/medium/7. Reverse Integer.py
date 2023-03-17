# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
#
#
# Constraints:
#
# -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        lesThenZero = 1
        if x < 0:
            lesThenZero = -1
            x *= -1
        xStr = str(x)
        xStr = xStr[::-1]
        result = int(xStr) * lesThenZero
        # 2**31 2147483648
        return result if -2**31 <= result <= 2**31 else 0


sol = Solution()
assert sol.reverse(1534236469) == 0
assert sol.reverse(-123) == -321
assert sol.reverse(-123) == -321
assert sol.reverse(123) == 321


class Solution2:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        result = 0
        while x:
            lastD = x % 10
            x //= 10
            result *= 10
            result += lastD
        result *= sign
        return result if -2**31 <= result <= 2**31 else 0


sol = Solution2()
assert sol.reverse(1534236469) == 0
assert sol.reverse(-123) == -321
assert sol.reverse(-123) == -321
assert sol.reverse(123) == 321
