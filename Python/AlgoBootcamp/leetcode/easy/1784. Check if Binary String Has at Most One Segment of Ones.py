# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:
#
# Input: s = "110"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


sol = Solution()
assert sol.checkOnesSegment("1001") is False
assert sol.checkOnesSegment("110") is True
