# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal
# substring
#  consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


sol = Solution()
assert sol.lengthOfLastWord("luffy is still joyboy ") == 6


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return l
            else:
                l += 1
        return l


sol = Solution2()
assert sol.lengthOfLastWord("luffy is still joyboy ") == 6
