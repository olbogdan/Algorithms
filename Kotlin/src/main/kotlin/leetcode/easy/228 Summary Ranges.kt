package leetcode.easy

import java.util.*

class `228 Summary Ranges` {

    fun summaryRanges(nums: IntArray): List<String> {
        if (nums.isEmpty()) {
            return emptyList()
        }

        val result = mutableListOf<String>()
        val stack = Stack<Long>()

        for (i in nums.indices) {
            val curInt = nums[i].toLong()



            if (stack.isNotEmpty() && curInt - stack.peek() > 1L) {
                dump(result, stack)
                stack.clear()
            }
            stack.push(curInt)
        }

        dump(result, stack)
        return result
    }

    fun dump(toArray: MutableList<String>, fromStack: Stack<Long>) {
        if (fromStack.size == 1) {
            toArray.add(fromStack.peek().toString())
        } else if (fromStack.size > 1) {
            val sb = StringBuilder().apply {
                append(fromStack.firstElement())
                append("->")
                append(fromStack.lastElement())
            }
            toArray.add(sb.toString())
        }
    }
}

fun main() {
    val solution = `228 Summary Ranges`()
    val result = solution.summaryRanges(intArrayOf(0, 2, 3, 4, 6, 8, 9))
    require(result == listOf("0", "2->4", "6", "8->9"))
}