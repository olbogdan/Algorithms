from typing import List

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#
#
# Example 1:
#
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
#
# Input: s = "a"
# Output: [["a"]]

def partition(s: str) -> List[List[str]]:
    result = []
    substring = []

    def dfs(i):
        if i >= len(s):
            result.append(substring.copy())
        for j in range(i, len(s)):
            if isPalindrome(s, i, j):
                substring.append(s[i:j + 1])
                dfs(j + 1)
                substring.pop()

    dfs(0)
    return result


def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

assert partition("aab") == [["a","a","b"],["aa","b"]]
assert partition("a") == [["a"]]