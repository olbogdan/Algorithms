# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        sArray = list(s)
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                sArray[l], sArray[r] = sArray[r], sArray[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowels:
                    l += 1
                if s[r] not in vowels:
                    r -= 1

        return "".join(sArray)


sol = Solution()
res = sol.reverseVowels("hello")
assert res == "holle"
