# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
#
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
#
# Return the sentence after the replacement.
#
#
#
# Example 1:
#
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:
#
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
#
#
# Constraints:
#
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.
from typing import List, Dict


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefixes = set(dictionary)

        def getShortVersion(word):
            for i in range(len(word)):
                if word[:i + 1] in prefixes:
                    return word[:i + 1]
            return word

        words = sentence.split(" ")
        resArray = []
        for w in words:
            newWord = getShortVersion(w)
            resArray.append(newWord)

        return " ".join(resArray)


sol = Solution()
assert sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert sol.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"


class Trie:
    def __init__(self, end: bool, continuation: Dict[str, 'Trie']):
        self.end = end
        self.continuation = continuation


class Solution2:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = self.createTrie(dictionary)

        def getShortVersion(word):
            level = trie
            for i in range(len(word)):
                char = word[i]
                if char in level:
                    if level[char].end:
                        return word[:i + 1]
                    level = level[char].continuation
                else:
                    return word

            return word

        words = sentence.split(" ")
        resArray = []
        for w in words:
            newWord = getShortVersion(w)
            resArray.append(newWord)

        return " ".join(resArray)

    def createTrie(self, dictionary: List[str]) -> Dict[str, Trie]:
        trie = {}
        for word in dictionary:
            level = trie
            for i in range(len(word)):
                char = word[i]
                if char not in level:
                    level[char] = Trie(False, {})

                if i == len(word) - 1:
                    level[char].end = True
                level = level[char].continuation
        return trie


sol = Solution2()
assert sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert sol.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"
