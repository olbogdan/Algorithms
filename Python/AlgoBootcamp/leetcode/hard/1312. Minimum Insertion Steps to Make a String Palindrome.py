# Given a string s. In one step you can insert any character at any index of the string.
#
# Return the minimum number of steps to make s palindrome.
#
# A Palindrome String is one that reads the same backward as well as forward.
#
#
#
# Example 1:
#
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:
#
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:
#
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.


class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def dp(l, r):
            if l >= r:
                return 0
            key = (l, r)
            if key in memo:
                return memo[key]

            if s[l] == s[r]:
                memo[key] = dp(l + 1, r - 1)
            else:
                memo[key] = 1 + min(dp(l + 1, r), dp(l, r - 1))
            return memo[key]
        return dp(0, len(s) - 1)


sol = Solution()
assert sol.minInsertions("leetcode") == 5
assert sol.minInsertions("mbadm") == 2
