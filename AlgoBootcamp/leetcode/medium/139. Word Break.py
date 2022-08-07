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
