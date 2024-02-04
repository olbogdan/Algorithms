# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
from cmath import inf
from collections import Counter, defaultdict


def minWindow(s: str, t: str) -> str:
    # s = "ADOBECODEBANC", t = "ABC"
    targetSub = {}
    currentSub = {}
    for char in t:
        targetSub[char] = targetSub.get(char, 0) + 1
        currentSub[char] = 0

    minResult = len(s)
    sub = []
    left = 0
    lengthOfSub = 0
    for right in range(len(s)):

        if s[right] in currentSub.keys():
            currentSub[s[right]] += 1
            if currentSub[s[right]] == targetSub[s[right]]:
                lengthOfSub += 1
        while lengthOfSub >= len(targetSub):
            if minResult > right - left:
                minResult = right - left
                sub = [left, right]

            if s[left] in currentSub.keys():
                currentSub[s[left]] -= 1
                if currentSub[s[left]] < targetSub[s[left]]:
                    lengthOfSub -= 1
            left += 1
    if len(sub) > 0:
        left = sub[0]
        right = sub[1] + 1
        return s[left:right]
    return ""


assert minWindow("ADOBECODEBANC","ABC") == "BANC"
assert minWindow("cabwefgewcwaefgcf", "cae") == "cwae"
assert minWindow("cabwefgewcwaefgcf", "x") == ""


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # use sliding window and a (counter or mask)
        mask1 = Counter(t)
        window = defaultdict(int)  # {char:count}

        def containAll():
            for char, count in mask1.items():
                if char not in window or window[char] < count:
                    return False
            return True

        l = r = 0
        shortest = float(inf)
        candidate = ""
        while r <= len(s):
            if not containAll():
                if r == len(s):
                    break
                window[s[r]] += 1
                r += 1
                continue
            if (r - l) < shortest:
                shortest = r - l
                candidate = s[l:r]
            window[s[l]] -= 1
            l += 1
        return candidate


assert Solution2().minWindow("ADOBECODEBANC","ABC") == "BANC"
