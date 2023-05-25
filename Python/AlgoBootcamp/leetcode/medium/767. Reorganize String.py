# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#
# Return any possible rearrangement of s or return "" if not possible.
#
#
#
# Example 1:
#
# Input: s = "aab"
# Output: "aba"
# Example 2:
#
# Input: s = "aaab"
# Output: ""
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = []
        for key, value in count.items():
            heappush(maxHeap, (-value, key)) # [countOfReps, character] [2, "a"], [1, "c"]

        N = len(s)
        resultArray = [""] * N

        count, char = heappop(maxHeap)
        # insert to odd spaces all chars starts from the biggest reps to lowest
        for i in range(0, N, 2):
            if count == 0:
                count, char = heappop(maxHeap)

            count += 1
            resultArray[i] = char
            if (i > 0 and resultArray[i - 1] == char) or (i < N - 2 and resultArray[i + 1] == char):
                return ""

        # insert to even spaces all chars starts from the biggest reps to lowest
        for i in range(1, N, 2):
            if count == 0:
                count, char = heappop(maxHeap)
            count += 1
            resultArray[i] = char
            if (i > 0 and resultArray[i - 1] == char) or (i < N - 2 and resultArray[i + 1] == char):
                return ""

        return "".join(resultArray)


sol = Solution()
res = sol.reorganizeString("caa")
assert res == "aca"
res = sol.reorganizeString("aaab")
assert res == ""
res = sol.reorganizeString("ababababb")
assert res == "babababab"
