package leetcode.medium

import java.util.PriorityQueue

class `2593 Find Score of an Array After Marking All Elements` {
    private data class Pairs(val value: Int, val idx: Int)

    fun findScore(nums: IntArray): Long {
        val visited = HashSet<Int>()
        val heap = PriorityQueue<Pairs> { a, b ->
            val valueDiff = a.value - b.value
            if (valueDiff != 0) {
                valueDiff
            } else {
                a.idx - b.idx
            }
        }
        nums.forEachIndexed { index, i ->
            heap.add(Pairs(value = i, idx = index))
        }
        var res = 0L
        while (heap.isNotEmpty()) {
            val (value, idx) = heap.remove()
            if (idx !in visited) {
                visited.add(idx - 1)
                visited.add(idx + 1)
                res += value
            }
        }

        return res
    }
}
