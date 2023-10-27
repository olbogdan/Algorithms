# Given a string s, return the longest palindromic substring in s.
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        L = 0
        R = 0
        def findLongest(l, r):
            nonlocal longest
            nonlocal L
            nonlocal R
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l > longest:
                longest = r - l
                L = l+1
                R = r-1
        for i in range(len(s)):
            findLongest(i, i)
            findLongest(i, i+1)
        return s[L:R+1]


sol = Solution()
assert sol.longestPalindrome("aacabdkacaa") == "aca"
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("a") == "a"


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        left = right = 0

        def expandSearch(l, r):
            nonlocal left, right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > right - left + 1:
                    left, right = l, r
                l -= 1
                r += 1

        for i in range(len(s)):
            expandSearch(i, i)
            expandSearch(i, i + 1)

        return s[left:right + 1]


sol = Solution3()
assert sol.longestPalindrome("aacabdkacaa") == "aca"
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("a") == "a"


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def isEqual(l, r):
            if l < 0 or l > len(s) - 1 or r < 0 or r > len(s) - 1:
                return False
            st = s[l:r+1]
            return st == st[::-1]

        memo = {}

        def expandSearch(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if isEqual(l, r):
                deepStr1 = expandSearch(l - 1, r + 1)
                deepStr2 = expandSearch(l, r + 1)
                deepStr3 = expandSearch(l - 1, r)
                res = max(deepStr1, deepStr2, deepStr3, key=len)
                if len(res) > 0:
                    memo[(l, r)] = res
                else:
                    memo[(l, r)] = s[l:r + 1]
                return memo[(l, r)]
            else:
                return ""

        result = ""
        for i in range(len(s)):
            innrStr = expandSearch(i, i)
            if len(innrStr) > len(result):
                result = innrStr
        return result


sol = Solution2()
assert sol.longestPalindrome("aacabdkacaa") == "aca"
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("a") == "a"