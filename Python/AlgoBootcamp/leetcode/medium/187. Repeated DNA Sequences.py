# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
#
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
#
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for left in range(len(s) - 9):
            subString = s[left:left + 10]
            if subString in seen:
                res.add(subString)
            else:
                seen.add(subString)
        return list(res)


sol = Solution()
res = sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
assert res == ["AAAAACCCCC","CCCCCAAAAA"]
