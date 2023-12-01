# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in order forms the string.
#
#
#
# Example 1:
#
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:
#
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:
#
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


class Solution2:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1i = 0
        sub1 = 0
        w2i = 0
        sub2 = 0
        while w1i < len(word1) and w2i < len(word2):
            if word1[w1i][sub1] != word2[w2i][sub2]:
                return False

            if sub2 + 1 == len(word2[w2i]):
                w2i += 1
                sub2 = 0
            else:
                sub2 += 1

            if sub1 + 1 == len(word1[w1i]):
                w1i += 1
                sub1 = 0
            else:
                sub1 += 1

        return w1i == len(word1) and w2i == len(word2)
