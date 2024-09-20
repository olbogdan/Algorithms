# You are given a string s. You can convert s to a
# palindrome
#  by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.
#
#
#
# Example 1:
#
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: s = "abcd"
# Output: "dcbabcd"
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 29
        lastIndex = 0
        power = 1
        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1
            prefix = prefix * base
            prefix = prefix + char
            suffix = suffix + char * power
            power = power * base
            if prefix == suffix:
                lastIndex = i
        suffix = s[lastIndex + 1:]
        return suffix[::-1] + s


sol = Solution()
assert sol.shortestPalindrome("aacecaaa") == "aaacecaaa"
assert sol.shortestPalindrome("abcd") == "dcbabcd"
