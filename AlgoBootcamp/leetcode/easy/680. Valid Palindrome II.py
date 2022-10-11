# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
#
# Input: s = "aba"
# Output: true
# Example 2:
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
#
# Input: s = "abc"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.


def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        else:
            left = s[l + 1:r + 1]
            right = s[l:r]
            if left == left[::-1] or right == right[::-1]:
                return True
            else:
                return False
    return True


assert validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") is True
assert validPalindrome("abca") is True
assert validPalindrome("abcca") is True
assert validPalindrome("abcbca") is True
assert validPalindrome("abcbxca") is False
