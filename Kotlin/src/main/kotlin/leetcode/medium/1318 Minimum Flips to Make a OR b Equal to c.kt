package leetcode.medium
/*Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.



Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0


Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9*/
class `1318 Minimum Flips to Make a OR b Equal to c` {
    fun minFlips(a: Int, b: Int, c: Int): Int {
        var result = 0
        var tempA = a
        var tempB = b
        var tempC = c

        while (tempA > 0 || tempB > 0 || tempC > 0) {
            val bitA = tempA and 1
            val bitB = tempB and 1
            val bitC = tempC and 1

            if (bitC == 0) {
                result += bitA + bitB
            } else if (bitC == 1) {
                if (bitA == 0 && bitB == 0) {
                    result += 1
                }
            }

            tempA = tempA shr 1
            tempB = tempB shr 1
            tempC = tempC shr 1
        }

        return result
    }
}
