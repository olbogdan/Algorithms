package leetcode.medium

import java.util.PriorityQueue

/**
 * A string s is called happy if it satisfies the following conditions:
 *
 * s only contains the letters 'a', 'b', and 'c'.
 * s does not contain any of "aaa", "bbb", or "ccc" as a substring.
 * s contains at most a occurrences of the letter 'a'.
 * s contains at most b occurrences of the letter 'b'.
 * s contains at most c occurrences of the letter 'c'.
 * Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
 *
 * A substring is a contiguous sequence of characters within a string.
 *
 *
 *
 * Example 1:
 *
 * Input: a = 1, b = 1, c = 7
 * Output: "ccaccbcc"
 * Explanation: "ccbccacc" would also be a correct answer.
 * Example 2:
 *
 * Input: a = 7, b = 1, c = 0
 * Output: "aabaa"
 * Explanation: It is the only correct answer in this case.
 *
 *
 * Constraints:
 *
 * 0 <= a, b, c <= 100
 * a + b + c > 0
 */

class `1405 Longest Happy String` {
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        val heap = PriorityQueue{ a : Pair<Int, Char>, b: Pair<Int, Char> ->
            b.first - a.first
        }
        if (a > 0) heap.add(a to 'a')
        if (b > 0) heap.add(b to 'b')
        if (c > 0) heap.add(c to 'c')

        val res = StringBuilder()
        while (heap.count() != 0) {
            val (count1, char1) = heap.poll()
            if (res.length >= 2 && res[res.count() - 1] == char1 && res[res.count() - 2] == char1) {
                if (heap.count() == 0) {
                    break
                }

                val (count2, char2) = heap.poll()
                res.append(char2)

                if (count2-1 > 0) {
                    heap.add(count2-1 to char2)
                }
                heap.add(count1 to char1)
            } else {
                res.append(char1)
                if (count1-1 > 0) {
                    heap.add(count1-1 to char1)
                }
            }
        }
        return res.toString()
    }
}

fun main() {
    val instance = `1405 Longest Happy String`()
    instance.longestDiverseString(1, 1, 7).also {
        println(it)
    }
}