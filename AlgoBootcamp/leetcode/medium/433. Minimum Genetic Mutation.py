# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
#
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be included in the bank.
# Example 1:
#
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:
#
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
#
#
# Constraints:
#
# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0] or str1[-1] != str2[-1]:
            return ""

        if len(str2) > len(str1):
            str1, str2 = str2, str1

        divider = len(str2)
        while divider > 0:
            candidate2 = str2[0:divider] * (len(str1) // divider)
            if str1 == candidate2:
                return str2[0:divider]

            divider -= 1
            while divider > 1 and (len(str1) % divider != 0 or len(str2) % divider != 0):
                divider -= 1
        return ""


sol = Solution()
res = sol.gcdOfStrings("ABCABC", "ABC")
assert res == "ABC"
res = sol.gcdOfStrings("ABCABCA", "A")
assert res == ""
