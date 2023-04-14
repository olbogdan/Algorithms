package leetcode.medium
/*Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
*/


class `516 Longest Palindromic Subsequence` {
    fun longestPalindromeSubseq(s: String): Int {
        val memo = mutableMapOf<Pair<Int, Int>, Int>()
        fun dp(l: Int, r: Int): Int {
            if (l > r) {
                return 0
            } else if (l == r) {
                return 1
            } else if (Pair(l, r) in memo) {
                return memo[Pair(l, r)]!!
            }

            val result = if (s[l] == s[r]) {
                2 + dp(l+1, r-1)
            } else {
                maxOf(dp(l+1, r), dp(l, r-1))
            }

            memo[Pair(l, r)] = result
            return result
        }

        return dp(0, s.length - 1)
    }
}

fun main() {
    val solution = `516 Longest Palindromic Subsequence`()

    // Test case 1: expected output is 4
    val s1 = "bbbab"
    val result1 = solution.longestPalindromeSubseq(s1)
    assert(result1 == 4)

    // Test case 2: expected output is 2
    val s2 = "cbbd"
    val result2 = solution.longestPalindromeSubseq(s2)
    assert(result2 == 2)
}