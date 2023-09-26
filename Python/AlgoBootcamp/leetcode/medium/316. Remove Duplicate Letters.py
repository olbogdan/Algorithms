# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
# the smallest in lexicographical order
#  among all possible results.
#
#
#
# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
#
# Input: s = "cbacdcbc"
# Output: "acdb"
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of lowercase English letters.
#
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        for c in s:
            while stack and c not in stack and stack[-1] >= c and count[stack[-1]] > 0:
                stack.pop()
            count[c] -= 1
            if c not in stack:
                stack.append(c)
        return "".join(stack)


sol = Solution()
assert sol.removeDuplicateLetters("abacb") == "abc"
