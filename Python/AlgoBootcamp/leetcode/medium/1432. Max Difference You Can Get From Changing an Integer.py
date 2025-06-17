# You are given an integer num. You will apply the following steps to num two separate times:
#
# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
#
# Return the max difference between a and b.
#
# Note that neither a nor b may have any leading zeros, and must not be 0.
#
#
#
# Example 1:
#
# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# Example 2:
#
# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
#
#
# Constraints:
#
# 1 <= num <= 108


class Solution:
    def maxDiff(self, num: int) -> int:
        numS = str(num)
        N = len(numS)
        firstNonNine = None
        minToSwap = numS[0] if numS[0] != '1' else None
        maxNumArr = []
        minNumArr = []

        for i in range(N):
            if firstNonNine is None and numS[i] != '9':
                firstNonNine = numS[i]
            if numS[i] == firstNonNine:
                maxNumArr.append('9')
            else:
                maxNumArr.append(numS[i])

            if minToSwap is None and numS[0] != numS[i] and numS[i] > '0':
                minToSwap = numS[i]
            if minToSwap is not None and minToSwap == numS[i]:
                minNumArr.append('1' if numS[0] == minToSwap else '0')
            else:
                minNumArr.append(numS[i])

        maxN = int(''.join(maxNumArr))
        minN = int(''.join(minNumArr))

        return maxN - minN


sol = Solution()
assert sol.maxDiff(555) == 888
assert sol.maxDiff(9) == 8
