# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#
#
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#
# Constraints:
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# -104 <= xn <= 104


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        def devidePow(x, n):
            if n == 1:
                return x
            half = devidePow(x, n//2)
            complete = half * half
            # multiply by x for odd
            if n % 2:
                complete *= x
            return complete

        result = devidePow(x, abs(n))
        if n < 0:
            return 1/result
        return result


sol = Solution()
res = sol.myPow(2, -2)
assert res == 0.25
res = sol.myPow(2.10000, 3)
assert res == 9.261000000000001
res = sol.myPow(0.44528, 0)
assert res == 1
res = sol.myPow(0.00001, 2147483647)
assert res == 0


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        sign = 1 if n > 0 else -1
        result = x
        for i in range(1, abs(n)):
            result *= x
        if sign < 0:
            return 1/result
        return result


sol = Solution2()
res = sol.myPow(2, -2)
assert res == 0.25
res = sol.myPow(2.10000, 3)
assert res == 9.261000000000001
res = sol.myPow(0.44528, 0)
assert res == 1
