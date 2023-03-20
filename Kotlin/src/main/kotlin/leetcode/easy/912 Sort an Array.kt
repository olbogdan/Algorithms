package leetcode.easy

import kotlin.test.assertEquals
import kotlin.test.assertTrue

class SortAnArray {
    fun sortArray(nums: IntArray): IntArray {

        fun merge(arr1: IntArray, arr2: IntArray, target: IntArray) {
            var i = 0
            var a1 = 0
            var a2 = 0

            while (a1 < arr1.size && a2 < arr2.size) {
                if (arr1[a1] < arr2[a2]) {
                    target[i] = arr1[a1]
                    a1 += 1
                } else {
                    target[i] = arr2[a2]
                    a2 += 1
                }
                i += 1
            }

            while (a1 < arr1.size) {
                target[i] = arr1[a1]
                a1 += 1
                i += 1
            }

            while (a2 < arr2.size) {
                target[i] = arr2[a2]
                a2 += 1
                i += 1
            }
        }

        fun sort(arr: IntArray): IntArray {
            if (arr.size < 2) {
                return arr
            }
            val mid = arr.size / 2
            val left = sort(arr.sliceArray(0 until mid))
            val right = sort(arr.sliceArray(mid until arr.size))
            merge(left, right, arr)
            return arr
        }

        return sort(nums)
    }
}


fun main() {
    val solution = SortAnArray()

    // Test case 1
    val arr = intArrayOf(5, 2, 3, 1)
    val result = solution.sortArray(arr)
    assertTrue(result contentEquals intArrayOf(1, 2, 3, 5))
}