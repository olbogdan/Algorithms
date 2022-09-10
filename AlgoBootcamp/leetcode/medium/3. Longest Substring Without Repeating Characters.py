# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    visited = set()
    result = 0
    left = 0
    for right in range(len(s)):
        while s[right] in visited:
            visited.remove(s[left])
            left += 1
        visited.add(s[right])
        result = max(result, len(visited))
    return result

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("babcd") == 4
assert lengthOfLongestSubstring("1") == 1
assert lengthOfLongestSubstring("") == 0

def lengthOfLongestSubstring2(s: str) -> int:
    if len(s) == 0:
        return 0

    visitedChar = set()
    result = 0
    visitedChar.add(s[0])
    # [b, a, c, a, x, c]
    left = 0
    right = 1
    while right < len(s):
        if s[right] not in visitedChar:
            visitedChar.add(s[right])
            right += 1
        else:
            result = max(result, len(visitedChar))
            while s[right] in visitedChar:
                visitedChar.remove(s[left])
                left += 1
            visitedChar.add(s[right])
            right += 1
    result = max(result, len(visitedChar))
    return result

assert lengthOfLongestSubstring2("abcabcbb") == 3
assert lengthOfLongestSubstring2("babcd") == 4
assert lengthOfLongestSubstring2("1") == 1
assert lengthOfLongestSubstring2("") == 0