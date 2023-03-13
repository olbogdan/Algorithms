# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs)

        for i in range(len(m)):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
        return m


sol = Solution()
res = sol.longestCommonPrefix(["flower","flow","flight"])
print(res)


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = max(strs)
        if len(m) == 0:
            return ""
        curIdx = 0
        while True:
            for s in strs:
                if curIdx == len(s) or s[curIdx] != m[curIdx]:
                    return m[:curIdx]
            curIdx += 1
        return m[:curIdx]


sol = Solution2()
res = sol.longestCommonPrefix(["flower","flow","flight"])
print(res)
