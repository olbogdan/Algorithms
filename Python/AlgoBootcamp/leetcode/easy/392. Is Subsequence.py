# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        sL, sR = 0, len(s) - 1
        tL, tR = 0, len(t) - 1
        while tL <= tR:
            if t[tL] == s[sL]:
                sL += 1
                tL += 1
                continue
            if t[tR] == s[sR]:
                sR -= 1
                tR -= 1
                continue
            if sL > sR:
                return True
            tL += 1
            tR -= 1
        return sL > sR


sol = Solution()
assert sol.isSubsequence("axc", "ahbxgdc") is True
assert sol.isSubsequence("axc", "ahbgdc") is False


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


sol = Solution2()
assert sol.isSubsequence("axc", "ahxbgdc") is True
assert sol.isSubsequence("axc", "ahbgdc") is False
