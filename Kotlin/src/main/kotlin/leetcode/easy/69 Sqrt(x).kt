package leetcode.easy
/*Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1*/

class `69 Sqrt(x)`  {
    fun mySqrt(x: Int): Int {
        var left = 0
        var right = x
        var result = 0
        while (left <= right) {
            val mid = left + (right - left) / 2
            val square = mid.toLong() * mid.toLong()
            when {
                square > x -> right = mid - 1
                square < x -> {
                    result = mid
                    left = mid + 1
                }
                else -> return mid
            }
        }
        return result
    }
}