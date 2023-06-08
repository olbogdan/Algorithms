# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
#
#
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
#
#
# Constraints:
#
# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        for i in range(len(num)):
            if not stack:
                stack.append(num[i])
                continue
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k > 0 and stack:
            stack.pop()
            k -= 1
        while stack and stack[0] == "0":
            stack.popleft()
        if not stack:
            stack.append("0")
        result = list(stack)
        return "".join(result)


sol = Solution()
assert sol.removeKdigits("1432219", 3) == "1219"
