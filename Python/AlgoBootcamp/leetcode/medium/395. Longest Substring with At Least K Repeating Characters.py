# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
#
# if no such substring exists, return 0.
#
#
#
# Example 1:
#
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105
from collections import Counter


class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        subArr = []
        for i in range(N):
            j = i
            while j < N and s[j] == s[i]:
                subArr.append((s[i], j - i + 1))
                j += 1
        count = Counter(subArr)
        res = -1
        for key, val in count.items():
            _, lenOfSequance = key
            if val >= 3:
                res = max(res, lenOfSequance)
        return res


sol = Solution()
assert sol.maximumLength("aaaa") == 2
assert sol.maximumLength("abcdef") == -1

