# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
# Note:
#
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will \
# be given as a signed integer type. It should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the
# input represents the signed integer. -3.
# Example 1:
#
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:
#
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:
#
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
#
#
# Constraints:
#
# The input must be a binary string of length 32.


class Solution:
    def hammingWeight(self, n) -> int:
        return n.bit_count()

# 1 loop
# 100001 minus 1
# 100000
# 100001 & 100000 = 100000
# 2 loop
# 100000 minus 1
# 011111
# 100000 & 011111 = 000000
# end loop, total count is 2
class Solution2:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result


# number >> 1 is the same as number / 2
# number % 2 == 1 the same as number & 1 == 1
class Solution3:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n & 1
            n = n >> 1
        return result


class Solution4:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n = n / 2
        return result
