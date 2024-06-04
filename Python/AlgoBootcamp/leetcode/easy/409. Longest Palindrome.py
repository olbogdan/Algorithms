# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#
#
#
# Example 1:
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        res = 0
        carry = 0
        for _, val in counter.items():
            if carry == 0 and val % 2 != 0:
                carry = 1
            if val > 1:
                res += (val // 2) * 2
        return res + carry


sol = Solution()
assert sol.longestPalindrome("abccccdd") == 7
assert sol.longestPalindrome("a") == 1
