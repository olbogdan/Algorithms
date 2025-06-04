# You are given a string word, and an integer numFriends.
#
# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
#
# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.
#
#
#
# Example 1:
#
# Input: word = "dbca", numFriends = 2
#
# Output: "dbc"
#
# Explanation:
#
# All possible splits are:
#
# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".
# Example 2:
#
# Input: word = "gggg", numFriends = 4
#
# Output: "g"
#
# Explanation:
#
# The only possible split is: "g", "g", "g", and "g".
#
#
#
# Constraints:
#
# 1 <= word.length <= 5 * 103
# word consists only of lowercase English letters.
# 1 <= numFriends <= word.length
from collections import deque


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        N = len(word)
        longestWindow = (N - numFriends + 1)

        def ifNewLonger(firstI, secondI):
            end = longestWindow
            if secondI + longestWindow > N:
                end = N - secondI

            for i in range(end):
                if word[firstI + i] > word[secondI + i]:
                    return False
                elif word[firstI + i] < word[secondI + i]:
                    return True
            return False

        mostCommon = max(word)
        resI = -1
        for i in range(N):
            if word[i] == mostCommon:
                if resI == -1 or ifNewLonger(resI, i):
                    resI = i
        return word[resI:min(resI + longestWindow, N)]


sol = Solution()
assert sol.answerString("epbbppl", 2) == "ppl"
assert sol.answerString("dbca", 2) == "dbc"


