# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.
# backtracking solution
from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)

        def isGood(word: str):
            if len(word) > len(chars):
                return False

            localCount = {}
            for c in word:
                localCount[c] = localCount.get(c, 0) + 1
                if localCount[c] > count.get(c, 0):
                    return False

            return True

        result = 0
        for w in words:
            if isGood(w):
                result += len(w)
        return result


sol = Solution()
assert sol.countCharacters(["cat","bt","hat","tree"], "atach") == 6
assert sol.countCharacters(["hello","world","leetcode"], "welldonehoneyr") == 10


class Solution1:
    def countCharacters(self, words: List[str], chars: str) -> int:

        result = 0
        for word in words:
            originalLen = len(word)
            library = Counter(chars)
            for char in word:
                if char in library and library[char] > 0:
                    library[char] -= 1
                    originalLen -= 1
                else:
                    break
            if originalLen == 0:
                result += len(word)

        return result


sol = Solution1()
assert sol.countCharacters(["cat","bt","hat","tree"], "atach") == 6
assert sol.countCharacters(["hello","world","leetcode"], "welldonehoneyr") == 10


class Solution2:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # adj = defaultdict(int)
        # for c in chars:
        #     adj[c] += 1
        adj = Counter(chars)
        result = 0

        def count(i, word, dictionaryCapacity):
            nonlocal result
            if i == len(word):
                return True
            if dictionaryCapacity == 0:
                return False

            if adj[word[i]] > 0:
                adj[word[i]] -= 1
                if count(i + 1, word, dictionaryCapacity - 1):
                    result += len(word)
                adj[word[i]] += 1
            else:
                return False

        for word in words:
            count(0, word, len(chars))

        return result


sol = Solution2()
assert sol.countCharacters(["cat","bt","hat","tree"], "atach") == 6
assert sol.countCharacters(["hello","world","leetcode"], "welldonehoneyr") == 10
