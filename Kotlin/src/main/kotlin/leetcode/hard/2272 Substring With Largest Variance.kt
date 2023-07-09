package leetcode.hard
/*The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.*/
class `2272 Substring With Largest Variance` {
    fun largestVariance(s: String): Int {
        var s = s
        var freq1 = 0
        var freq2 = 0
        var variance = 0

        // create distinct list of character pairs
        val pairs = s.toSet().flatMap { l1 -> s.toSet().mapNotNull { l2 -> if (l1 != l2) Pair(l1, l2) else null } }

        // run once for original string order, then again for reverse string order
        repeat(2) {
            for (pair in pairs) {
                s.forEach { letter ->
                    // no reason to process letters that aren't part of the current pair
                    val (first, second) = pair
                    if (letter != first && letter != second) {
                        return@forEach
                    }

                    if (letter == pair.first) {
                        freq1 += 1
                    } else if (letter == pair.second) {
                        freq2 += 1
                    }

                    if (freq1 < freq2) {
                        freq1 = 0
                        freq2 = 0
                    } else if (freq1 > 0 && freq2 > 0) {
                        variance = maxOf(variance, freq1 - freq2)
                    }
                }

                freq1 = 0
                freq2 = 0
            }

            // reverse the string for the second time around
            s = s.reversed()
        }

        return variance
    }
}

fun main() {
    val sol = `2272 Substring With Largest Variance`()
    require(sol.largestVariance("aababbb") == 3)
}