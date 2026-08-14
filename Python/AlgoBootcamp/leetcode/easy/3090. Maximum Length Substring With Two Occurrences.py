# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
#
#
# Example 1:
#
# Input: s = "bcbbbcba"
#
# Output: 4
#
# Explanation:
#
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:
#
# Input: s = "aaaa"
#
# Output: 2
#
# Explanation:
#
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
#
#
# Constraints:
#
# 2 <= s.length <= 100
# s consists only of lowercase English letters.
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        visit = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            visit[s[r]] += 1
            while visit[s[r]] > 2:
                visit[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


assert Solution().maximumLengthSubstring("bcbbbcba") == 4
assert Solution().maximumLengthSubstring("aaaa") == 2