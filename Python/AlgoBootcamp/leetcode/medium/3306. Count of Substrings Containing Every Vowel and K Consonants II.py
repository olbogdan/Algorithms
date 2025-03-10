# You are given a string word and a non-negative integer k.
#
# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
#
#
#
# Example 1:
#
# Input: word = "aeioqq", k = 1
#
# Output: 0
#
# Explanation:
#
# There is no substring with every vowel.
#
# Example 2:
#
# Input: word = "aeiou", k = 0
#
# Output: 1
#
# Explanation:
#
# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
#
# Example 3:
#
# Input: word = "ieaouqqieaouqq", k = 1
#
# Output: 3
#
# Explanation:
#
# The substrings with every vowel and one consonant are:
#
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
#
#
# Constraints:
#
# 5 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5
from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        vowelCount = defaultdict(int)
        consonCount = 0
        l = 0
        res = 0
        leadingVowel = 0
        for r in range(len(word)):
            char = word[r]
            if char in vowel:
                vowelCount[char] += 1
            else:
                consonCount += 1
            while consonCount > k or (consonCount == k and l < len(word) and word[l] in  vowelCount and vowelCount[word[l]] > 1):
                charRemove = word[l]
                l += 1
                if charRemove in vowelCount:
                    vowelCount[charRemove] -= 1
                    if vowelCount[charRemove] == 0:
                        del vowelCount[charRemove]
                    else:
                        leadingVowel += 1
                else:
                    leadingVowel = 0
                    consonCount -= 1

            if consonCount == k and len(vowelCount) == 5:
                res = res + leadingVowel + 1
        return res


sol = Solution()
assert sol.countOfSubstrings("aeioqq", 1) == 0
assert sol.countOfSubstrings("aeiou", 0) == 1
assert sol.countOfSubstrings("ieaouqqieaouqq", 1) == 3
