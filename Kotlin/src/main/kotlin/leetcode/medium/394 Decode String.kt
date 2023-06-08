package leetcode.medium

import kotlin.time.times

/*Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
*/


class `394 Decode String2` {
    var index = 0

    fun decodeString(s: String): String {
        val decoded = StringBuilder()

        while (index < s.length && s[index] != ']') {
            if (!s[index].isDigit()) {
                decoded.append(s[index++])
            } else {
                var k = 0
                while (index < s.length && s[index].isDigit()) {
                    k = k * 10 + (s[index++] - '0')
                }

                // case: [
                index++
                val answer = decodeString(s)

                // case: ]
                index++

                // add k*encoded to decoded
                repeat(k) {
                    decoded.append(answer)
                }
            }
        }

        return decoded.toString()
    }
}


class `394 Decode String` {
    fun decodeString(s: String): String {
        val stackNumbers = mutableListOf<String>()
        val result = StringBuilder()
        var i = 0

        while (i < s.length) {
            val ch = s[i]
            if (ch.isDigit()) {
                stackNumbers.add(ch.toString())
            } else if (ch == '[') {
                val number = stackNumbers.joinToString("").toInt()
                stackNumbers.clear()
                var openBraces = 1
                var j = i + 1
                val subResult = StringBuilder()

                while (openBraces != 0) {
                    if (s[j] == ']') {
                        openBraces -= 1
                    } else if (s[j] == '[') {
                        openBraces += 1
                    }
                    j += 1
                }

                subResult.append(decodeString(s.substring(i+1, j-1)))
                repeat(number) {
                    result.append(subResult)
                }

                i = j
                continue
            } else if (ch != ']') {
                result.append(ch)
            }
            i += 1
        }
        return result.toString()
    }
}
