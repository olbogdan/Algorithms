package leetcode.medium
/*There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.3
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100.
*/
class `62 Unique Paths` {

    fun uniquePaths(m: Int, n: Int): Int {

        val R = m
        val C = n

        val memo = HashMap<Pair<Int, Int>, Int>()

        fun dp(r: Int, c: Int): Int {
            if (r == R || c == C) return 0
            if (r == R - 1 && c == C - 1) return 1

            if (Pair(r, c) in memo) {
                return memo[Pair(r, c)]!!
            }

            memo[Pair(r, c)] = dp(r, c + 1) + dp(r + 1, c)
            return memo[Pair(r, c)]!!
        }

        return dp(0, 0)
    }

}