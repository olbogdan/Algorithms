# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        result = []
        for i in range(len(a)):
            c1 = int(a[i])
            c2 = 0
            if i < len(b):
                c2 = int(b[i])
            comby = carry + c1 + c2
            result.append(str(comby % 2))
            carry = comby // 2

        if carry != 0:
            result.append("1")
        result.reverse()
        return "".join(result)


sol = Solution()
res = sol.addBinary("11", "1")
assert res == "100"
res = sol.addBinary("111", "1010")
assert res == "10001"
