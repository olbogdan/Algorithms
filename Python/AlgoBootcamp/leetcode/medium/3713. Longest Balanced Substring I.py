# You are given a string s consisting of lowercase English letters.
#
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
#
# Return the length of the longest balanced substring of s.
#
#
#
# Example 1:
#
# Input: s = "abbac"
#
# Output: 4
#
# Explanation:
#
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
#
# Example 2:
#
# Input: s = "zzabccy"
#
# Output: 4
#
# Explanation:
#
# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​
#
# Example 3:
#
# Input: s = "aba"
#
# Output: 2
#
# Explanation:
#
# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
#
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for l in range(len(s)):
            count = defaultdict(int)
            for r in range(l, len(s)):
                count[s[r]] += 1
                if len(set(count.values())) == 1:
                    res = max(res, r - l + 1)

        return res


sol = Solution()
assert sol.longestBalanced("abbac") == 4
assert sol.longestBalanced("zzabccy") == 4
assert sol.longestBalanced("aba") == 2
