# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
#
# Example 1:
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
# Constraints:
#
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        def sameStr(L, R) -> bool:
            i = 0
            while L <= R:
                if needle[i] != haystack[L]:
                    return False
                i += 1
                L += 1
            return True

        needleKey = 0
        hayStKey = 0
        for i in range(len(needle)):
            needleKey += ord(needle[i])
            hayStKey += ord(haystack[i])

        L = 0
        R = len(needle) - 1
        while R < len(haystack):
            if needleKey == hayStKey and sameStr(L, R):
                return L
            else:
                hayStKey -= ord(haystack[L])
                L += 1
                R += 1
                if R < len(haystack):
                    hayStKey += ord(haystack[R])
        return -1


sol = Solution()
assert sol.strStr("aaa", "aaaa") == -1
assert sol.strStr("aaaa", "aaaa") == 0
assert sol.strStr("aababa", "ba") == 2
