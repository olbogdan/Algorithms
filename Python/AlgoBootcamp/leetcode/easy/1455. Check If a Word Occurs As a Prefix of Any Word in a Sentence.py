# Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.
#
# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
#
# A prefix of a string s is any leading contiguous substring of s.
#
#
#
# Example 1:
#
# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
# Example 2:
#
# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
# Example 3:
#
# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.
#
#
# Constraints:
#
# 1 <= sentence.length <= 100
# 1 <= searchWord.length <= 10
# sentence consists of lowercase English letters and spaces.
# searchWord consists of lowercase English letters.


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        N = len(searchWord)
        for w in words:
            if len(w) < N:
                continue
            i = 0
            while i <= N:
                if i == N:
                    return words.index(w) + 1
                if w[i] != searchWord[i]:
                    break
                i += 1
        return -1


sol = Solution()
assert sol.isPrefixOfWord("i love eating burger", "burg") == 4
assert sol.isPrefixOfWord("this problem is an easy problem", "pro") == 2
