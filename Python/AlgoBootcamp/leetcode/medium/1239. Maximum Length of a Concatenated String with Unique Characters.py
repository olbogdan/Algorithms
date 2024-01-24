# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
#
#
# Constraints:
#
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = self.createMasksArray(arr)
        ONES = '1'

        def dp(i, mask):
            if i == len(masks):
                return bin(mask).count(ONES)

            canTake = True if mask & masks[i] == 0 else False

            result = dp(i + 1, mask)
            if canTake:
                result = max(result, dp(i + 1, mask | masks[i]))
            return result

        return dp(0, 0)

    def createMasksArray(self, arr) -> List[set]:
        result = set()
        for string in arr:
            candidate = 0
            charRepeats = False
            for c in string:
                cMask = 1 << ord(c)
                if cMask & candidate != 0:
                    charRepeats = True
                    break
                candidate = candidate | cMask
            if not charRepeats:
                result.add(candidate)
        return list(result)

