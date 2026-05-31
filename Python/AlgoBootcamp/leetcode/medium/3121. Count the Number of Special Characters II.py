# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
#
# Return the number of special letters in word.
#
#
#
# Example 1:
#
# Input: word = "aaAbcBC"
#
# Output: 3
#
# Explanation:
#
# The special characters are 'a', 'b', and 'c'.
#
# Example 2:
#
# Input: word = "abc"
#
# Output: 0
#
# Explanation:
#
# There are no special characters in word.
#
# Example 3:
#
# Input: word = "AbBCab"
#
# Output: 0
#
# Explanation:
#
# There are no special characters in word.
#
#
#
# Constraints:
#
# 1 <= word.length <= 2 * 105
# word consists of only lowercase and uppercase English letters.


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        visit = {}
        for idx, ch in enumerate(word):
            if ch == ch.upper():
                if ch not in visit:
                    visit[ch] = idx
            else:
                visit[ch] = idx
        res = 0
        for chIdx in range(ord('a'), ord('z')+1):
            ch = chr(chIdx)
            if ch in visit and ch.upper() in visit and visit[ch] < visit[ch.upper()]:
                res += 1
        return res


sol = Solution()
assert sol.numberOfSpecialChars("aaAbcBC") == 3
assert sol.numberOfSpecialChars("a") == 0
assert sol.numberOfSpecialChars("abc") == 0