# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings
#  respectively, such that:
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.
#
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
# Example 3:
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
# Constraints:
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory space?
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dp(i1, i2, i3):
            if i1 == len(s1) and i2 == len(s2):
                return True
            left = False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                left = dp(i1 + 1, i2, i3 + 1)
            right = False
            if i2 < len(s2) and s2[i2] == s3[i3]:
                right = dp(i1, i2 + 1, i3 + 1)
            return left or right

        return dp(0, 0, 0)


sol = Solution()
assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
assert sol.isInterleave("a", "a", "aa") is True
assert sol.isInterleave("", "", "") is True
assert sol.isInterleave("", "", "d") is False


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dp(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True

            if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dp(i1 + 1, i2):
                return True
            if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dp(i1, i2 + 1):
                return True
            return False
        return dp(0, 0)


sol = Solution2()
assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
assert sol.isInterleave("a", "a", "aa") is True
assert sol.isInterleave("", "", "") is True
assert sol.isInterleave("", "", "d") is False
