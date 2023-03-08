# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #            2 3 4
        #            3 2 1
        # mult1      2 3 4 (1*4, 1*3, 1*2) idx i(0) + j
        # mult2    4 6 8   (2*4, 2*3, 2*2) idx i(1) + j
        # mult3  7 0 2     (3*4, 3*3 (1 carry), 3*2 (1 carry))
        # sum    7 5 1 1 4 (4, 3+8(1carry)) etc 75114
        if num1[0] == "0" or num2[0] == "0":
            return "0"
        resArr = [0]*(len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                resIdx = i + j
                prevCarry = resArr[resIdx]
                prod = int(num1[i]) * int(num2[j]) + prevCarry
                nextCarry = prod // 10
                resArr[resIdx+1] += nextCarry
                resArr[resIdx] = prod % 10

        # remove leading zeros (from the end coz reversed)  [2,3,4,0,0]
        # reverse result and convert to str
        res = ""
        for i in range(len(resArr)-1, -1, -1):
            if resArr[i] == 0 and len(res) == 0:
                continue
            res += str(resArr[i])

        return res


sol = Solution()
assert sol.multiply("123", "456") == "56088"
assert sol.multiply("2", "3") == "6"
assert sol.multiply("30256", "999") == "30225744"
