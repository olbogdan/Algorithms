package leetcode.easy
/*A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.



Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Constraints:

2 <= arr.length <= 1000
-106 <= arr[i] <= 106*/

class `1502 Can Make Arithmetic Progression From Sequence` {
    fun canMakeArithmeticProgression(arr: IntArray): Boolean {
        arr.sort()
        val step = arr[1] - arr[0]
        for (i in 1 until arr.size) {
            if (step != arr[i] - arr[i - 1]) {
                return false
            }
        }
        return true
    }
}

fun main() {
    val solution = `1502 Can Make Arithmetic Progression From Sequence`()
    val arr1 = intArrayOf(3, 5, 1)
    val arr2 = intArrayOf(3, 5, 1, 1)
    require(solution.canMakeArithmeticProgression(arr1)) { "Test case 1 failed" }
    require(!solution.canMakeArithmeticProgression(arr2)) { "Test case 2 failed" }
}
