package leetcode.medium

class `2425 Bitwise XOR of All Pairings` {
    fun xorAllNums(nums1: IntArray, nums2: IntArray): Int {
        var res = 0
        if (nums1.count() % 2 == 1) {
            nums2.forEach {
                res = res xor it
            }
        }
        if (nums2.count() % 2 == 1) {
            nums1.forEach {
                res = res xor it
            }
        }
        return res
    }
}