package leetcode.medium

import kotlin.math.pow

/*Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.



Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation:
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011".
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".


Constraints:

1 <= low <= high <= 105
1 <= zero, one <= low*/
class `2466 Count Ways To Build Good Strings` {
    fun countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int {
        val MOD = 1_000_000_007
        val n = high
        val memo = mutableMapOf(0 to 1)
        var result = 0

        for (i in 1..n) {
            memo[i] = (memo.getOrDefault(i - zero, 0) +
                    memo.getOrDefault(i - one, 0)) % MOD

            if (i >= low) {
                result += memo[i]!!
                result %= MOD
            }
        }

        return result % MOD
    }
}

class `2466 Count Ways To Build Good Strings2` {
    fun countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int {
        val MOD = 10.0.pow(9.0).toInt() + 7
        val memo = HashMap<Int, Long>()
        fun dp(len: Int): Long {
            if (len > high) {
                return 0
            }
            if (len in memo) {
                return memo.getOrDefault(len, Long.MAX_VALUE)
            }
            var res = 0L
            if (len >= low) {
                res++
            }
            res += dp(len+zero)
            res += dp(len+one)
            res = res % MOD
            memo[len] = res
            return res
        }
        return (dp(0) % MOD).toInt()
    }
}