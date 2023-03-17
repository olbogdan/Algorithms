# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    memo = {}
    for ch in s:
        if ch in memo:
            memo[ch] = memo[ch] + 1
        else:
            memo[ch] = 1

    for ch in t:
        if ch not in memo or memo[ch] == 0:
            return False
        else:
            memo[ch] -= 1

    return True


assert isAnagram("anagram", "nagaram") == True
assert isAnagram("aab", "abb") == False
