# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
#
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
# Constraints:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0] or str1[-1] != str2[-1]:
            return ""

        if len(str2) > len(str1):
            str1, str2 = str2, str1

        divider = len(str2)
        while divider > 0:
            candidate2 = str2[0:divider] * (len(str1) // divider)
            if str1 == candidate2:
                return str2[0:divider]

            divider -= 1
            while divider > 1 and (len(str1) % divider != 0 or len(str2) % divider != 0):
                divider -= 1
        return ""


sol = Solution()
res = sol.gcdOfStrings("ABCABC", "ABC")
assert res == "ABC"
res = sol.gcdOfStrings("ABCABCA", "A")
assert res == ""
