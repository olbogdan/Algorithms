# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#
# Constraints:
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # convert the wordlist to an hashmap
        # iterate for loop on beginWord indexes
        # iterate in a nested for loop on char a - z
        # replace each index by each char
        # check if this word exist in the hashmap
        # if new word == endWord return its transformation len + 1
        # add the found word into a bfsQueue with its transformation len + 1
        # remove the word from wordList because it is visited
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque()
        q.append((beginWord, 1)) # (node, transforLen)
        while q:
            word, transforLen = q.popleft()
            for i in range(len(beginWord)):
                for c in range(ord("a"), ord("z") + 1):
                    # i = 0 "abc"  [:i] + X + [i+1:] -> "Xbc"
                    # i = 2 "abc"  [:i] + X + [i+1:] -> "abX"
                    newWord = word[:i] + chr(c) + word[i+1:]
                    if newWord in wordSet:
                        if newWord == endWord:
                            return transforLen + 1
                        wordSet.remove(newWord)
                        q.append((newWord, transforLen + 1))
        return 0


sol = Solution()
res = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(res)
