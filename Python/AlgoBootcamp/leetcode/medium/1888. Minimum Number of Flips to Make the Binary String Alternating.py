# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
#
# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
#
# The string is called alternating if no two adjacent characters are equal.
#
# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
#
#
# Example 1:
#
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
# Example 2:
#
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# Example 3:
#
# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
from cmath import inf


class Solution:
    def minFlips(self, s: str) -> int:
        template1 = [i % 2 for i in range(len(s) * 2)]
        template2 = [i % 2 for i in range(1, (len(s) * 2 + 1))]
        src = [int(char) for char in s]
        src += src

        res = float(inf)
        alternating1 = 0
        alternating2 = 0
        for i in range(len(src)):
            if template1[i] != src[i]:
                alternating1 += 1
            if template2[i] != src[i]:
                alternating2 += 1

            # "abcA(3)bc" len 3 - idx3 == 0, remove 0
            left = i - len(s)
            if left >= 0:
                if template1[left] != src[left]:
                    alternating1 -= 1
                if template2[left] != src[left]:
                    alternating2 -= 1
            if i >= len(s) - 1:
                res = min(res, alternating1, alternating2)
        return res


sol = Solution()
assert sol.minFlips("1110") == 1
