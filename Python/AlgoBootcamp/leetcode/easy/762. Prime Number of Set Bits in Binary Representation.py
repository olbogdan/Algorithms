# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.
#
# Recall that the number of set bits an integer has is the number of 1's present when written in binary.
#
# For example, 21 written in binary is 10101, which has 3 set bits.
#
#
# Example 1:
#
# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.
# Example 2:
#
# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 5 numbers have a prime number of set bits.
#
#
# Constraints:
#
# 1 <= left <= right <= 106
# 0 <= right - left <= 104

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 10^3=1000 10^6=1000.000 (2^10=1024) ~ doulbe it 2^20 ~= 1000.000
        primArr = self.primes(21)
        res = 0
        for n in range(left, right + 1):
            bits = self.numOfSetBits(n)
            if primArr[bits]:
                res += 1
        return res

    def numOfSetBits(self, number):
        res = 0
        while number != 0:
            if number & 1 == 1:
                res += 1
            number = number >> 1
        return res

    def primes(self, upperBound: int) -> [int]:
        if upperBound <= 1:
            return [False, False]

        arr = [True] * upperBound
        arr[0] = False
        arr[1] = False

        i = 2
        while i * i < upperBound:
            if arr[i] == True:
                for j in range(i * i, upperBound, i):
                    arr[j] = False
            i += 1

        return arr


sol = Solution()
assert sol.countPrimeSetBits(6, 10) == 4
assert sol.countPrimeSetBits(10, 15) == 5
