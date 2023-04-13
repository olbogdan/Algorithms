package leetcode.medium
/*Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.*/
import java.util.*

class `946 Validate Stack Sequences` {
    fun validateStackSequences(pushed: IntArray, popped: IntArray): Boolean {
        val stack = ArrayDeque<Int>()
        var pushedIdx = 0
        var poppedIdx = 0

        while (poppedIdx < popped.size && pushedIdx < pushed.size) {
            stack.push(pushed[pushedIdx])
            pushedIdx++

            while (stack.isNotEmpty() && stack.peek() == popped[poppedIdx]) {
                stack.pop()
                poppedIdx++
            }
        }

        return stack.isEmpty()
    }
}


fun main() {
    val solution = `946 Validate Stack Sequences`()

    val pushed1 = intArrayOf(1, 2, 3, 4, 5)
    val popped1 = intArrayOf(4, 5, 3, 2, 1)
    val result1 = solution.validateStackSequences(pushed1, popped1)
    assert(result1)

    val pushed2 = intArrayOf(1, 2, 3, 4, 5)
    val popped2 = intArrayOf(4, 3, 5, 1, 2)
    val result2 = solution.validateStackSequences(pushed2, popped2)
    assert(!result2)
}