package leetcode.hard


import kotlin.math.*

class `1187 Make Array Strictly Increasing` {
    fun makeArrayIncreasing(arr1: IntArray, arr2: IntArray): Int {
        val list2 = arr2.distinct().sorted()
        val INV = -1
        val cache = Array(arr1.size + 1) { Array(list2.size + 1) { IntArray(2) { -2 } } }

        fun dfs(pos1: Int, pos2: Int, skipped: Int): Int {
            val prev = if (skipped == 1) arr1.getOrElse(pos1 - 1) { -1 } else list2.getOrElse(pos2 - 1) { -1 }
            return if (pos1 == arr1.size) 0 else cache[pos1][pos2][skipped].takeIf { it != -2 }
                ?: if (pos2 == list2.size) {
                    if (arr1[pos1] > prev) dfs(pos1 + 1, pos2, 1) else INV
                } else if (list2[pos2] <= prev) {
                    dfs(pos1, pos2 + 1, 1)
                } else {
                    val replace = dfs(pos1 + 1, pos2 + 1, 0)
                    val skip = if (arr1[pos1] > prev) dfs(pos1 + 1, pos2, 1) else INV
                    if (skip != INV && replace != INV) minOf(skip, 1 + replace)
                    else if (replace != INV) 1 + replace else skip
                }.also { cache[pos1][pos2][skipped] = it }
        }

        return dfs(0, 0, 1)
    }
}
fun main() {
    val sol = `1187 Make Array Strictly Increasing`()
    println(
        sol.makeArrayIncreasing(
            intArrayOf(13, 2, 17, 2, 1, 8, 7, 10, 3, 12, 7, 20, 13),
            intArrayOf(25, 16, 17, 10, 25, 18, 13, 8, 3, 22, 1, 20, 13, 18, 25, 20, 11, 18, 15, 12)
        )
    )
    require(sol.makeArrayIncreasing(intArrayOf(13,2,17,2,1,8,7,10,3,12,7,20,13), intArrayOf(25,16,17,10,25,18,13,8,3,22,1,20,13,18,25,20,11,18,15,12)) == 11)
    require(sol.makeArrayIncreasing(intArrayOf(0,11,6,1,4,3), intArrayOf(5,4,11,10,1,0)) == 5)
    require(sol.makeArrayIncreasing(intArrayOf(1,5,3,6,7), intArrayOf(4,3,1)) == 2)
}