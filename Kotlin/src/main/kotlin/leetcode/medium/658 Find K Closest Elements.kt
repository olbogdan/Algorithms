package leetcode.medium
/*Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104*/

import kotlin.math.*
class `658 Find K Closest Elements` {
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        var L = 0
        var R = k - 1
        while (R < arr.size - 1) {
            val leftDistance = abs(x - arr[L])
            val rightDistance = abs(x - arr[R + 1])
            if (arr[L] != arr[R + 1] && leftDistance <= rightDistance) {
                return arr.sliceArray(L..R).toList()
            }
            R++
            L++
        }
        return arr.sliceArray(L..R).toList()
    }
}

fun main() {
    val sol = `658 Find K Closest Elements`()
    assert(sol.findClosestElements(intArrayOf(1,1,1,10,10,10), 1, 9) == listOf(10))
    assert(sol.findClosestElements(intArrayOf(1,2,3,4,5), 4, 3) == listOf(1,2,3,4))
}