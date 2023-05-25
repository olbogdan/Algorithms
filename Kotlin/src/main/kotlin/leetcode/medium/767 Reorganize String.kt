package leetcode.medium
/*Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.*/

import java.util.*
import kotlin.collections.HashMap

class `767 Reorganize String` {
    fun reorganizeString(s: String): String {
        val count = HashMap<Char, Int>()
        for (c in s) {
            count[c] = count.getOrDefault(c, 0) + 1
        }

        val maxHeap = PriorityQueue<Pair<Int, Char>>(compareBy({ -it.first }, { it.second }))
        for ((key, value) in count) {
            maxHeap.offer(value to key)
        }

        val n = s.length
        val resultArray = Array(n) { "" }

        var (countValue, char) = maxHeap.poll()
        // insert to odd spaces all chars starts from the biggest reps to lowest
        for (i in 0 until n step 2) {
            if (countValue == 0) {
                val pair = maxHeap.poll()
                countValue = pair.first
                char = pair.second
            }

            countValue--
            resultArray[i] = char.toString()
            if ((i > 0 && resultArray[i - 1] == char.toString()) || (i < n - 2 && resultArray[i + 1] == char.toString())) {
                return ""
            }
        }

        // insert to even spaces all chars starts from the biggest reps to lowest
        for (i in 1 until n step 2) {
            if (countValue == 0) {
                val pair = maxHeap.poll()
                countValue = pair.first
                char = pair.second
            }

            countValue--
            resultArray[i] = char.toString()
            if ((i > 0 && resultArray[i - 1] == char.toString()) || (i < n - 2 && resultArray[i + 1] == char.toString())) {
                return ""
            }
        }

        return resultArray.joinToString("")
    }
}

fun main() {
    val sol = `767 Reorganize String`()
    var res = sol.reorganizeString("caa")
    assert(res == "aca")
    res = sol.reorganizeString("aaab")
    assert(res == "")
    res = sol.reorganizeString("ababababb")
    assert(res == "babababab")
}