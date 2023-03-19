package leetcode.easy

import java.lang.Integer.min
import kotlin.test.assertEquals

/*Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.*/


class Solution3 {
    fun maxNumberOfBalloons(text: String): Int {
        val charRep = text.groupingBy { it }.eachCount()
        var minRep = Int.MAX_VALUE
        val repeatedChar = setOf('l', 'o')
        for (c in "balon") {
            val reps = charRep[c] ?: 0
            minRep = if (c in repeatedChar) {
                println(reps / 2)
                min(minRep, reps / 2)
            } else {
                min(minRep, reps)
            }
        }
        return minRep
    }
}

fun main() {
    val solution = Solution3()
    assertEquals(solution.maxNumberOfBalloons("lll"),0)
}