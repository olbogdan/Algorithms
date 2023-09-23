# You are given an array of words where each word consists of lowercase English letters.
#
# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
#
# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
#
# Return the length of the longest possible word chain with words chosen from the given list of words.
#
#
#
# Example 1:
#
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
# Example 2:
#
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# Example 3:
#
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
#
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        buckets = {}  # {len : list(words)}
        longest = 0
        for w in words:
            longest = max(longest, len(w))
            if len(w) not in buckets:
                buckets[len(w)] = set()
            buckets[len(w)].add(w)

        dp = {}

        def findLongestChain(word) -> int:
            if word in dp:
                return dp[word]
            longest = 1
            if len(word) - 1 in buckets:
                for child in buckets[len(word) - 1]:
                    if isChild(child, word):
                        longest = max(longest, 1 + findLongestChain(child))
            dp[word] = longest
            return longest

        def isChild(shortW, longW) -> bool:
            iS = 0
            iL = 0
            diff = 0
            while iS < len(shortW):
                if shortW[iS] == longW[iL]:
                    iS += 1
                    iL += 1
                else:
                    if diff == 1:
                        return False
                    diff += 1
                    iL += 1
            return diff <= 1

        result = 1
        for i in buckets.keys():
            if i - 1 in buckets:
                for word in buckets[i]:
                    result = max(result, findLongestChain(word))
        return result


sol = Solution()
assert sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5
