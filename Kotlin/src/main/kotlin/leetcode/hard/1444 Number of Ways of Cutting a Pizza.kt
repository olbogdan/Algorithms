package leetcode.hard

class `1444 Number of Ways of Cutting a Pizza` {
    private val MOD = 1000000007

    fun ways(pizza: Array<String>, k: Int): Int {
        val rows = pizza.size
        val cols = pizza[0].length

        val appleCount = Array(rows) { IntArray(cols) }
        for (i in rows - 1 downTo 0) {
            var count = 0
            for (j in cols - 1 downTo 0) {
                if (pizza[i][j] == 'A') count++
                if (i < rows - 1) appleCount[i][j] += appleCount[i + 1][j]
                appleCount[i][j] += count
            }
        }

        val memo = Array(rows) { Array(cols) { IntArray(k) { -1 } } }
        fun dp(r: Int, c: Int, cutsLeft: Int): Int {
            if (cutsLeft == 0) {
                return if (appleCount[r][c] > 0) 1 else 0
            }
            if (memo[r][c][cutsLeft - 1] != -1) {
                return memo[r][c][cutsLeft - 1]
            }
            var ans = 0
            for (i in r + 1 until rows) {
                if (appleCount[r][c] - appleCount[i][c] > 0) {
                    ans = (ans + dp(i, c, cutsLeft - 1)) % MOD
                }
            }
            for (j in c + 1 until cols) {
                if (appleCount[r][c] - appleCount[r][j] > 0) {
                    ans = (ans + dp(r, j, cutsLeft - 1)) % MOD
                }
            }
            memo[r][c][cutsLeft - 1] = ans
            return ans
        }

        return dp(0, 0, k - 1)
    }
}



fun main() {
    val sol = `1444 Number of Ways of Cutting a Pizza`()
    assert(sol.ways(arrayOf("A..", "AAA", "..."), 3) == 3)
    assert(sol.ways(arrayOf("A..", "AA.", "..."), 3) == 1)
}