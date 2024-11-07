package leetcode.medium

import kotlin.math.max

class `2275 Largest Combination With Bitwise AND Greater Than Zero` {

    fun largestCombination(candidates: IntArray): Int {
        val maxVal = candidates.max()
        var i = 1
        var res = 0
        while (i <= maxVal) {
            var curRes = 0
            candidates.forEach {
                if (it and i > 0) {
                    curRes++
                }
            }
            i = i shl 1
            res = max(res, curRes)
        }
        return res
    }
}