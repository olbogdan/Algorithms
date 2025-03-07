# Given two positive integers left and right, find the two integers num1 and num2 such that:
#
# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
#
#
#
# Example 1:
#
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:
#
# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
#
#
# Constraints:
#
# 1 <= left <= right <= 106
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def createPrimes() -> List[int]:
            erat = [True] * (right + 1)
            erat[0] = erat[1] = False
            for n in range(2, right//2):
                if erat[n] is False:
                    continue
                runN = n + n
                while runN < len(erat):
                    erat[runN] = False
                    runN = runN + n
            res = []
            for i in range(len(erat)):
                if left <= i <= right and erat[i] is True:
                    res.append(i)
            return res

        primes = createPrimes()
        res = [-1, -1]
        distance = float('inf')
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < distance:
                distance = primes[i] - primes[i-1]
                res = [primes[i-1], primes[i]]
        return res


sol = Solution()
# assert sol.closestPrimes(10, 19) == [11,13]
# assert sol.closestPrimes(4, 6) == [-1,-1]
# assert sol.closestPrimes(1, 1) == [-1,-1]
assert sol.closestPrimes(18, 72) == [29,31]
