package leetcode.medium

class `983 Minimum Cost For Tickets` {

    fun mincostTickets(days: IntArray, costs: IntArray): Int {
        fun getNextI(i: Int, offset: Int): Int {
            var nextI = i
            val coveredDays = days[i] + offset
            while (nextI < days.count() && days[nextI] < coveredDays) {
                nextI++
            }
            return nextI
        }
        val memo = HashMap<Int, Int>()
        fun dp(i: Int): Int {
            if (i >= days.count()) {
                return 0
            }
            if (i in memo) {
                return memo.get(i)!!
            }
            val res1 = costs[0] + dp(i+1)
            val res2 = costs[1] + dp(getNextI(i, 7))
            val res3 = costs[2] + dp(getNextI(i, 30))
            val res = Math.min(res1, Math.min(res2, res3))
            memo[i] = res
            return res
        }
        return dp(0)
    }
}
