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
    right = 0
    result = 0
    charCount = {}

    def maxFrequent():
        maxFr = 0
        for ch, fr in charCount.items():
            maxFr = max(maxFr, fr)
        return maxFr

    # abc 1
    while right < len(s):
        charCount[s[right]] = charCount.get(s[right], 0) + 1
        if right - left - k < maxFrequent():
            result = max(result, right - left + 1)
        else:
            while right - left - k >= maxFrequent():
                charCount[s[left]] = charCount[s[left]] - 1
                left += 1
        right += 1

    return result


assert characterReplacement("ABBB", 2) == 4
assert characterReplacement("ABAB", 2) == 4
assert characterReplacement("AABABBA", 1) == 4
assert characterReplacement("AABABBA", 0) == 2
assert characterReplacement("AAAAAAB", 1) == 7

