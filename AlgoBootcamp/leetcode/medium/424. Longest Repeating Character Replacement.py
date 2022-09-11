# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


def characterReplacement(s: str, k: int) -> int:
    left = 0
    result = 0
    charCount = {}

    for r in range(len(s)):
        charCount[s[r]] = charCount.get(s[r], 0) + 1
        maxFr = max(charCount.values())
        if r - left + 1 - maxFr > k:
            charCount[s[left]] = charCount[s[left]] - 1
            left += 1
        result = max(result, r - left + 1)

    return result


assert characterReplacement("ABBB", 2) == 4
assert characterReplacement("ABAB", 2) == 4
assert characterReplacement("AABABBA", 1) == 4
assert characterReplacement("AABABBA", 0) == 2
assert characterReplacement("AAAAAAB", 1) == 7

