package leetcode.hard

class `41 First Missing Positive` {

    fun firstMissingPositive(nums: IntArray): Int {
        val N = nums.size

        // clean up input from invalid nums, replace minuses in [-1, -2, 0, 3, 4] by 0
        for (i in 0 until N) {
            if (nums[i] < 0) {
                nums[i] = 0
            }
        }

        // use minus value to indicate that item at position i exist
        // associate mapping [idx0 = val 1, idx1 = val 2]
        for (i in 0 until N) {
            val value = Math.abs(nums[i])
            // value in valid range
            if (0 < value && value <= N) {
                val idxToInvert = value - 1
                if (nums[idxToInvert] > 0) {
                    nums[idxToInvert] *= -1
                } else if (nums[idxToInvert] == 0) {
                    nums[idxToInvert] = Int.MIN_VALUE
                }
            }
        }

        // we get a cache as [-1, -3, -2147483648, -2] means all values 1 to N exist - the answer N+1
        // we get a cache as [-1, 4, -2147483648, -2] means value 2 does not exist, return it
        // [-1, -4, 0, -2] 0 means at position is not found, return idx of val 0 + 1
        for (i in 0 until N) {
            if (nums[i] >= 0) {
                return i + 1
            }
        }
        return N + 1
    }
}

fun main() {
    val solution = `41 First Missing Positive`()

    assert(solution.firstMissingPositive(intArrayOf(1, 2, 3)) == 4)
    assert(solution.firstMissingPositive(intArrayOf(2, -1, 4, 0)) == 1)
}