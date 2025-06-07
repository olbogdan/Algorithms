# You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.
#
# While there is a '*', do the following operation:
#
# Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
# Return the lexicographically smallest resulting string after removing all '*' characters.
#
#
#
# Example 1:
#
# Input: s = "aaba*"
#
# Output: "aab"
#
# Explanation:
#
# We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.
#
# Example 2:
#
# Input: s = "abc"
#
# Output: "abc"
#
# Explanation:
#
# There is no '*' in the string.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters and '*'.
# The input is generated such that it is possible to delete all '*' characters.


class Solution:
    def clearStars(self, s: str) -> str:
        N = ord('z') - ord('a') + 1
        count = [ [] for _ in range(N)] # char, arr of index
        def getMinCharGroupIdx():
            for i in range(N):
                if len(count[i]) > 0:
                    return i
            return None

        removed = set()
        for i in range(len(s)):
            if s[i] == '*':
                group = getMinCharGroupIdx()
                if group is not None:
                    removed.add(count[group].pop())
            else:
                count[ord(s[i]) - ord('a')].append(i)
        res = []
        for i in range(len(s)):
            if s[i] != '*' and i not in removed:
                res.append(s[i])
        return "".join(res)


sol = Solution()
assert sol.clearStars("aaba*") == "aab"
assert sol.clearStars("abc") == "abc"
