# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 105
# s consists of only lowercase English letters.
from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unicC = { ch for ch in s }

        left = set()

        right = Counter(s)

        result = set()
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
                unicC.remove(s[i])
            for ch in unicC:
                if ch in left and ch in right:
                    # optimisation. We also can store string concat "rightMleft"
                    result.add((s[i],ch))
            left.add(s[i])
        return len(result)


sol = Solution()
res = sol.countPalindromicSubsequence("abc")
assert res == 0
res = sol.countPalindromicSubsequence("abca")
assert res == 2


class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = {}
        for i in reversed(range(len(s))):
            if s[i] not in right:
                right[s[i]] = i
        left = set()
        res = set()
        for i in range(len(s)):
            if s[i] in right.keys() and right[s[i]] == i:
                del right[s[i]]
            for ch in left:
                if ch in left and ch in right.keys():
                    res.add(ch + s[i])
            left.add(s[i])
        return len(res)


sol = Solution2()
assert sol.countPalindromicSubsequence("bbcbaba") == 4
assert sol.countPalindromicSubsequence("adc") == 0
assert sol.countPalindromicSubsequence("aabca") == 3
