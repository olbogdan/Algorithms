# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
#
# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?
#
#
#
# Example 1:
#
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# Example 2:
#
# Input: strs = ["omv","ovm"]
# Output: 1
#
#
# Constraints:
#
# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] consists of lowercase letters only.
# All words in strs have the same length and are anagrams of each other.
# @unionjoin
from typing import List


class Union:

    def __init__(self, size):
        self.parents = list(range(size))

    def find(self, i) -> int:
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def join(self, i, j):
        rootI = self.find(i)
        rootJ = self.find(j)
        if rootI != rootJ:
            self.parents[rootI] = rootJ

    def countOfGroups(self) -> int:
        count = 0
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                count += 1
        return count


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        N = len(strs)
        union = Union(N)

        for i in range(N):
            for j in range(i + 1, N):
                if isSimilar(strs[i], strs[j]):
                    union.join(i, j)

        return union.countOfGroups()


sol = Solution()
assert sol.numSimilarGroups(["tars","rats","arts","star"]) == 2
assert sol.numSimilarGroups(["omv","ovm"]) == 1


class Solution2:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if not visited[j] and is_similar(strs[i], strs[j]):
                    dfs(j)

        n = len(strs)
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count


sol = Solution2()
assert sol.numSimilarGroups(["tars","rats","arts","star"]) == 2
assert sol.numSimilarGroups(["omv","ovm"]) == 1
