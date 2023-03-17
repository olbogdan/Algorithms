# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
#
#
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
# Constraints:
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
# #DP
from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 = "aa" text2 == "bbb"
        # [[0, 0]
        # [0, 0]
        # [0, 0]]
        cache = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    cache[j][i] = 1 + cache[j+1][i+1]
                else:
                    cache[j][i] = max(cache[j+1][i], cache[j][i+1])
        return cache[0][0]


sol = Solution()
res = sol.longestCommonSubsequence("abc", "abc")
assert res == 3
res = sol.longestCommonSubsequence("ace", "abcde")
assert res == 3
res = sol.longestCommonSubsequence("xha", "abcde")
assert res == 1


class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            if text1[i1] == text2[i2]:
                return 1 + dp(i1 + 1, i2 + 1)
            else:
                return max(dp(i1 + 1, i2), dp(i1, i2 + 1))
        return dp(0, 0)


sol = Solution1()
res = sol.longestCommonSubsequence("abc", "abc")
assert res == 3
res = sol.longestCommonSubsequence("ace", "abcde")
assert res == 3
res = sol.longestCommonSubsequence("xha", "abcde")
assert res == 1


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(t1, t2):
            if len(t1) == 0 or len(t2) == 0:
                return 0
            if t1[0] == t2[0]:
                return 1 + dp(t1[1:], t2[1:])
            else:
                return max(dp(t1[1:], t2), dp(t1, t2[1:]))

        return dp(text1, text2)


sol = Solution2()
res = sol.longestCommonSubsequence("abc", "abc")
assert res == 3
res = sol.longestCommonSubsequence("ace", "abcde")
assert res == 3
res = sol.longestCommonSubsequence("xha", "abcde")
assert res == 1
