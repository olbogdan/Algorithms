package leetcode.medium
/*Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length*/
class `1456 Maximum Number of Vowels in a Substring of Given Length` {

    fun maxVowels(s: String, k: Int): Int {
        val N = s.length
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        var r = 0
        var l = 0
        var result = 0
        var curSum = 0
        while (r < N) {
            if (s[r] in vowels) {
                curSum++
            }
            if (r - l == k) {
                if (s[l] in vowels) {
                    curSum--
                }
                l++
            }
            r++
            result = maxOf(result, curSum)
        }
        return result
    }
}