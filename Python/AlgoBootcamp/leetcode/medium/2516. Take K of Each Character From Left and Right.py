# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
#
# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
#
#
#
# Example 1:
#
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation:
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.
# Example 2:
#
# Input: s = "a", k = 1
# Output: -1
# Explanation: It is not possible to take one 'b' or 'c' so return -1.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only the letters 'a', 'b', and 'c'.
# 0 <= k <= s.length
from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        N = len(s)
        count = Counter(s)
        for char in ['a', 'b', 'c']:
            if char not in count:
                return -1
        if not self.isValid(count, k):
            return -1
        res = N
        l = 0
        for r in range(N):
            count[s[r]] -= 1
            while not self.isValid(count, k):
                count[s[l]] += 1
                l += 1
            res = min(res, N - (r - l + 1))
        return res

    def isValid(self, count, k):
        for key, val in count.items():
            if val < k:
                return False
        return True


sol = Solution()
print(sol.takeCharacters("abc", 1))