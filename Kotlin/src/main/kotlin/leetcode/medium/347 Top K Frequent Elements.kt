package leetcode.medium

class `347 Top K Frequent Elements` {

    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val numReps = nums.fold(mutableMapOf<Int, Int>()) { count, num ->
            count[num] = count.getOrDefault(num, 0) + 1
            count
        }
        val repsToNum = mutableMapOf<Int, MutableList<Int>>()
        for ((num, reps) in numReps) {
            repsToNum.getOrPut(reps) { mutableListOf() }.add(num)
        }

        val result = mutableListOf<Int>()
        for (i in nums.size downTo 0) {
            if (i in repsToNum) {
                for (num in repsToNum[i]!!) {
                    if (result.size == k) {
                        return result.toIntArray()
                    }
                    result.add(num)
                }
            }
        }
        return result.toIntArray()
    }
}

fun main() {
    val sol = `347 Top K Frequent Elements`()
    var res = sol.topKFrequent(intArrayOf(1), 1)
    assert(res.contentEquals(intArrayOf(1)))
    assert(sol.topKFrequent(intArrayOf(-1, -1), 1).contentEquals(intArrayOf(-1)))
}