package leetcode.medium
/*Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.*/

import java.util.*
class `402 Remove K Digits` {

    fun removeKdigits(num: String, k: Int): String {
        var k = k
        val stack = Stack<Char>()
        for (i in num.indices) {
            if (stack.isEmpty()) {
                stack.push(num[i])
                continue
            }
            while (stack.isNotEmpty() && stack.peek() > num[i] && k > 0) {
                stack.pop()
                k--
            }
            stack.push(num[i])
        }

        while (k > 0 && stack.isNotEmpty()) {
            stack.pop()
            k--
        }

        while (stack.isNotEmpty() && stack.firstElement() == '0') {
            stack.removeAt(0)
        }

        if (stack.isEmpty()) {
            stack.push('0')
        }
        return stack.joinToString("")
    }
}
