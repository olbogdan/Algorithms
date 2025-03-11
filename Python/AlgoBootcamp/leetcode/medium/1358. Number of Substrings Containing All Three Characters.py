# Given a string s consisting only of characters a, b and c.
#
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
#
#
#
# Example 1:
#
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
# Example 2:
#
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
# Example 3:
#
# Input: s = "abc"
# Output: 1
#
#
# Constraints:
#
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = m = 0
        res = 0
        count = {} # char : num of reps
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            charToRemove = s[m]
            while count.get(charToRemove, 0) > 1:
                count[charToRemove] -= 1
                m += 1
                charToRemove = s[m]
            if len(count) == 3:
                res += 1 + (m - l)

        return res


sol = Solution()
assert sol.numberOfSubstrings("abcabc") == 10
assert sol.numberOfSubstrings("aaacb") == 3
