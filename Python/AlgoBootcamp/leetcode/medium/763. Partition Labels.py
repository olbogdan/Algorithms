# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#
# Return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        debt = set()
        result = []
        size = 0
        for i in range(len(s)):
            char = s[i]
            size += 1
            count[char] -= 1
            if count[char] > 0:
                debt.add(char)
            else:
                if char in debt:
                    debt.remove(char)
                if not debt:
                    result.append(size)
                    size = 0
        return result


sol = Solution()
assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9,7,8]
assert sol.partitionLabels("eccbbbbdec") == [10]


class Solution2:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            char = s[i]
            lastIdx[char] = i

        end = 0
        size = 0
        result = []
        for i in range(len(s)):
            size += 1
            char = s[i]
            end = max(end, lastIdx[char])
            if end == i:
                result.append(size)
                size = 0

        return result


sol = Solution2()
assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9,7,8]
assert sol.partitionLabels("eccbbbbdec") == [10]
