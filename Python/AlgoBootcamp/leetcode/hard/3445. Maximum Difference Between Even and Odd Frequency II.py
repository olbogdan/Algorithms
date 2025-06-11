# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:
#
# subs has a size of at least k.
# Character a has an odd frequency in subs.
# Character b has an even frequency in subs.
# Return the maximum difference.
#
# Note that subs can contain more than 2 distinct characters.
#
#
#
# Example 1:
#
# Input: s = "12233", k = 4
#
# Output: -1
#
# Explanation:
#
# For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.
#
# Example 2:
#
# Input: s = "1122211", k = 3
#
# Output: 1
#
# Explanation:
#
# For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.
#
# Example 3:
#
# Input: s = "110", k = 3
#
# Output: -1
#
#
#
# Constraints:
#
# 3 <= s.length <= 3 * 104
# s consists only of digits '0' to '4'.
# The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
# 1 <= k <= s.length
from collections import defaultdict


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        N = len(s)
        res = float('-inf')

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                s1 = [0] * (N + 1)
                s2 = [0] * (N + 1)

                for i in range(1, N + 1):
                    s1[i] = s1[i - 1] + (int(s[i - 1]) == a)
                    s2[i] = s2[i - 1] + (int(s[i - 1]) == b)

                g = [[float('-inf')] * 2 for _ in range(2)]
                j = 0

                for i in range(k, N + 1):
                    while i - j >= k and s1[i] > s1[j] and s2[i] > s2[j]:
                        pa = s1[j] % 2
                        pb = s2[j] % 2
                        g[pa][pb] = max(g[pa][pb], s2[j] - s1[j])
                        j += 1

                    pa = s1[i] % 2
                    pb = s2[i] % 2
                    best = g[1 - pa][pb]
                    if best != float('-inf'):
                        res = max(res, (s1[i] - s2[i]) + best)

        return -1 if res == float('-inf') else res


sol = Solution()
assert sol.maxDifference("12233", 4) == -1
assert sol.maxDifference("1122211", 3) == 1
assert sol.maxDifference("110", 3) == -1