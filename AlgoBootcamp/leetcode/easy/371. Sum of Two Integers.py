# Given two integers a and b, return the sum of the two integers without using the operators + and -.
#
#
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
# -1000 <= a, b <= 1000
#         1.Why carry is a&b:
#         If a and b are both 1 at the same digit, it creates one carry.
#         Because you can only use 0 and 1 in binary, if you add 1+1 together, it will roll that over to the next digit, and the value will be 0 at this digit.
#         if they are both 0 or only one is 1, it doesn't need to carry.

#         Use ^ operation between a and b to find the different bit
#         In my understanding, using ^ operator is kind of adding a and b together (a+b) but ignore the digit that a and b are both 1,
#         because we already took care of this in step1.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # for overflow condition like -1/1
        return a & mask if b > mask else a


sol = Solution()
assert sol.getSum(1, 2) == 3
assert sol.getSum(10, 10) == 20
