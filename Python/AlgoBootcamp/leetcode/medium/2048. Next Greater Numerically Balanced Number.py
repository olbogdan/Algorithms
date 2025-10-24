# An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.
#
# Given an integer n, return the smallest numerically balanced number strictly greater than n.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 22
# Explanation:
# 22 is numerically balanced since:
# - The digit 2 occurs 2 times.
# It is also the smallest numerically balanced number strictly greater than 1.
# Example 2:
#
# Input: n = 1000
# Output: 1333
# Explanation:
# 1333 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 1000.
# Note that 1022 cannot be the answer because 0 appeared more than 0 times.
# Example 3:
#
# Input: n = 3000
# Output: 3133
# Explanation:
# 3133 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 3000.
#
#
# Constraints:
#
# 0 <= n <= 106
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        num = n + 1
        while True:
            if self.isNumericallyBalanced(num):
                return num
            num += 1

    def isNumericallyBalanced(self, num: int) -> bool:
        counts = Counter(str(num))
        for digitChar, count in counts.items():
            if int(digitChar) != count:
                return False
        return True


sol = Solution()
assert sol.nextBeautifulNumber(1000) == 1333
assert sol.nextBeautifulNumber(3000) == 3133
