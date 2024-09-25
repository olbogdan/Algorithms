# You are given an array words of size n consisting of non-empty strings.
#
# We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
#
# For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
# Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
#
# Note that a string is considered as a prefix of itself.
#
#
#
# Example 1:
#
# Input: words = ["abc","ab","bc","b"]
# Output: [5,4,3,2]
# Explanation: The answer for each string is the following:
# - "abc" has 3 prefixes: "a", "ab", and "abc".
# - There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
# The total is answer[0] = 2 + 2 + 1 = 5.
# - "ab" has 2 prefixes: "a" and "ab".
# - There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
# The total is answer[1] = 2 + 2 = 4.
# - "bc" has 2 prefixes: "b" and "bc".
# - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
# The total is answer[2] = 2 + 1 = 3.
# - "b" has 1 prefix: "b".
# - There are 2 strings with the prefix "b".
# The total is answer[3] = 2.
# Example 2:
#
# Input: words = ["abcd"]
# Output: [4]
# Explanation:
# "abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
# Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
#
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists of lowercase English letters.
from collections import defaultdict
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        count = defaultdict(int)
        for w in words:
            for i in range(1, len(w)+1):
                count[w[:i]] += 1
        res = []
        for w in words:
            subRes = 0
            for i in range(1, len(w)+1):
                subRes += count[w[:i]]
            res.append(subRes)
        return res


sol = Solution()
assert sol.sumPrefixScores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]


class Node:
    def __init__(self, char: str):
        self.char = char
        self.neighbors = []
        self.count = 1

    def insert(self, node: 'Node'):
        exist = self.getNode(node.char)
        if exist:
            exist.count += 1
        else:
            self.neighbors.append(node)

    def getNode(self, char: str) -> 'Node':
        for neighbor in self.neighbors:
            if neighbor.char == char:
                return neighbor
        return None


class Solution2:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes = self.createPrefixTree(words)

        res = []
        for w in words:
            curSum = 0
            curRoot = prefixes
            for i in range(len(w)):
                curRoot = curRoot.getNode(w[i])
                curSum += curRoot.count
            res.append(curSum)
        return res

    def createPrefixTree(self, words: List[str]):
        root = Node("")
        for w in words:
            curRoot = root
            for i in range(len(w)):
                nextNode = Node(w[i])
                curRoot.insert(nextNode)
                curRoot = curRoot.getNode(w[i])
        return root


sol = Solution2()
assert sol.sumPrefixScores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
