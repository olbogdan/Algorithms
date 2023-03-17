# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    lenS = len(s)
    dp = [False] * (lenS + 1)
    dp[0] = True
    for i in range(lenS + 1):
        if not dp[i]:
            continue
        for word in wordDict:
            if i + len(word) < lenS + 1 and s[i:i + len(word)] == word:
                dp[i + len(word)] = dp[i]

    return dp[lenS]


assert wordBreak("aaaaaaa", ["aaaa", "aaa"])
assert wordBreak("a", ["a"])
assert wordBreak("leetcode", ["leetc", "leet", "cod", "e"])


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}  # index - Bool, True if can be reached

        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            result = False
            for w in wordDict:
                # w is smaller than remaining len and == to s's substring
                # [b, a(i)] compare to a(w), len(w)1+1 <= 2
                if len(w) + i <= len(s) and s[i:len(w)+i] == w:
                    if dp(i + len(w)):
                        result = True
            memo[i] = result
            return result

        return dp(0)


sol = Solution()
res = sol.wordBreak("leetcode", ["leet","code"])
assert res is True


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def isEquals(iStart, word) -> bool:
            endOfW = len(word) + iStart
            if endOfW <= len(s):
                sW = s[iStart:endOfW]
                return sW == word

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for w in wordDict:
                    if isEquals(i, w):
                        dp[i+len(w)] = True

        return dp[-1]


sol = Solution2()
res = sol.wordBreak("leetcode", ["leet","code"])
assert res is True

