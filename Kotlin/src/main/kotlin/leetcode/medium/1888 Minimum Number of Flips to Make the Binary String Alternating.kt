package leetcode.medium
/*You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.


Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".


Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
*/
class `1888 Minimum Number of Flips to Make the Binary String Alternating` {
    fun minFlips(s: String): Int {
        val template1 = (0 until s.length * 2).map { i -> i % 2 }
        val template2 = (1..s.length * 2).map { i -> i % 2 }
        val src = s.map { char -> char.toString().toInt() }.toMutableList()
        src += src

        var res = Double.POSITIVE_INFINITY
        var alternating1 = 0
        var alternating2 = 0
        for (i in src.indices) {
            if (template1[i] != src[i]) {
                alternating1 += 1
            }
            if (template2[i] != src[i]) {
                alternating2 += 1
            }

            // "abcA(3)bc" len 3 - idx3 == 0, remove 0
            val left = i - s.length
            if (left >= 0) {
                if (template1[left] != src[left]) {
                    alternating1 -= 1
                }
                if (template2[left] != src[left]) {
                    alternating2 -= 1
                }
            }
            if (i >= s.length - 1) {
                res = minOf(res, alternating1.toDouble(), alternating2.toDouble())
            }
        }
        return res.toInt()
    }
}
