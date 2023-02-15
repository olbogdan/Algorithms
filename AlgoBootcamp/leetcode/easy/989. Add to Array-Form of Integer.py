# The array-form of an integer num is an array representing its digits in left to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
# Example 1:
#
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# Example 2:
#
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# Example 3:
#
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
#
# Constraints:
#
# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 104
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        i = 0
        while k:
            dig = k % 10

            if i < len(num):
                num[i] += dig
            else:
                num.append(dig)

            # 12 // 10 == 1 | 7 // 10 == 0
            carry = num[i] // 10
            # 12 % 10 == 2
            num[i] = num[i] % 10
            k = k // 10
            k += carry
            i += 1

        num.reverse()
        return num


sol = Solution()
res = sol.addToArrayForm([2,7,4], 181)
assert res == [4,5,5]
sol = Solution()
res = sol.addToArrayForm([2,1,5], 806)
assert res == [1,0,2,1]


class Solution2:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numStr = ""
        for n in num:
            numStr += str(n)
        numInt = int(numStr)
        resultInt = numInt + k
        resultStr = str(resultInt)
        resultArr = []
        for s in resultStr:
            resultArr.append(int(s))
        return resultArr


sol = Solution2()
res = sol.addToArrayForm([2,7,4], 181)
assert res == [4,5,5]
sol = Solution()
res = sol.addToArrayForm([2,1,5], 806)
assert res == [1,0,2,1]
