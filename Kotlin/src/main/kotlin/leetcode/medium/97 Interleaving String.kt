package leetcode.medium
import kotlin.collections.mutableMapOf

class `97 Interleaving String` {
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        if (s1.length + s2.length != s3.length) {
            return false
        }
        val memo = mutableMapOf<Pair<Int, Int>, Boolean>()

        fun dp(i1: Int, i2: Int, i3: Int): Boolean {
            if (i3 == s3.length) {
                return true
            }
            val key = Pair(i1, i2)
            if (key in memo) {
                return memo[key] ?: false
            }
            var result = false
            if (i1 < s1.length && s1[i1] == s3[i3]) {
                if (dp(i1 + 1, i2, i3 + 1)) {
                    memo[key] = true
                    return true
                }
            }
            if (i2 < s2.length && s2[i2] == s3[i3]) {
                if (dp(i1, i2 + 1, i3 + 1)) {
                    memo[key] = true
                    return true
                }
            }
            memo[key] = false
            return false
        }

        return dp(0, 0, 0)
    }
}