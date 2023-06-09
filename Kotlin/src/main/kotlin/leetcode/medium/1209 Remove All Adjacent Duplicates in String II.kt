package leetcode.medium

import java.util.*

class `1209 Remove All Adjacent Duplicates in String II` {
    fun removeDuplicates(s: String, k: Int): String {
        val stack = Stack<Pair<Char, Int>>()
        for (char in s) {
            if (stack.isNotEmpty() && stack.peek().first == char) {
                val count = stack.pop().second + 1
                if (count < k) {
                    stack.push(Pair(char, count))
                }
            } else {
                stack.push(Pair(char, 1))
            }
        }

        val sb = StringBuilder()
        while (stack.isNotEmpty()) {
            val pair = stack.pop()
            sb.append(pair.first.toString().repeat(pair.second))
        }
        return sb.reverse().toString()
    }
}

fun main() {
    val sol = `1209 Remove All Adjacent Duplicates in String II`()
    val res = sol.removeDuplicates("deeedbbcccbdaa", 3)
    assert(res == "aa") { "Test case failed" }
}
