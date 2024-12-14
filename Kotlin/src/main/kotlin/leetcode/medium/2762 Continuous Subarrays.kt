package leetcode.medium

import java.util.*


class `2762 Continuous Subarrays` {
    private data class Pair(val value: Int, val index: Int)

    fun continuousSubarrays(nums: IntArray): Long {
        var res = 0L
        var l = 0
        val minHeap = PriorityQueue<Pair>() { a, b ->
            return@PriorityQueue if (a.value == b.value) {
                a.index - b.index
            } else {
                a.value - b.value
            }
        }
        val maxHeap = PriorityQueue<Pair>() { a, b ->
            return@PriorityQueue if (a.value == b.value) {
                a.index - b.index
            } else {
                b.value - a.value
            }
        }

        for (r in 0..<nums.count()) {
            minHeap.offer(Pair(nums[r], r))
            maxHeap.offer(Pair(nums[r], r))
            while (minHeap.isNotEmpty() && maxHeap.peek().value - minHeap.peek().value > 2) {
                l++
                while (minHeap.peek().index < l) {
                    minHeap.remove()
                }
                while (maxHeap.peek().index < l) {
                    maxHeap.remove()
                }
            }
            res += (r - l + 1)
        }
        return res
    }
}

fun main() {
    val instance = `2762 Continuous Subarrays`()
    assert(instance.continuousSubarrays(intArrayOf(1, 2, 3)) == 6L)
    assert(instance.continuousSubarrays(intArrayOf(2, 2, 2)) == 6L)
}
