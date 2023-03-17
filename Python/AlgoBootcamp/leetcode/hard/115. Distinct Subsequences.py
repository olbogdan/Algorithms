# Given two strings s and t, return the number of distinct
# subsequences
#  of s which equals t.
#
# The test cases are generated so that the answer fits on a 32-bit signed integer.
#
#
#
# Example 1:
#
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:
#
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.
from functools import cache


# Similar to 1143. Longest Common Subsequence. Recursively sum the solution of the two equations.
# If it was possible to reach the end of the string T. This means that at least one subsequence was found.


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(sI, tI):
            # success: reached the end of the searching string T
            if tI == len(t):
                return 1
            elif sI == len(s):
                return 0
            if s[sI] == t[tI]:
                # 2 cases: 1) take this item. 2) ignore coz in feature maybe more subsequences:
                # example: s = "rab(1 case)b(2 case)it" t = "rabbit"
                return dp(sI+1, tI+1) + dp(sI+1, tI)
            else:
                return dp(sI+1, tI)
        return dp(0, 0)


sol = Solution()
assert sol.numDistinct("babgbag", "bag") == 5
assert sol.numDistinct("rabbbit", "rabbit") == 3
