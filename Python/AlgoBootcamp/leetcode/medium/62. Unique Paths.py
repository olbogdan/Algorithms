# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
#
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
# Example 2:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
# Constraints:
#
# 1 <= m, n <= 100


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R = m
        C = n

        dp = [0] * C
        dp[-1] = 1
        # 1 Last row: [0, 0, 0, 1] i == last -> ignore
        # 2 Last row: [0, 0, 1, 1] i == 2 -> take cur value + value at right
        # result is at dp[0]
        for _ in range(R):
            for col in reversed(range(C)):
                dp[col] = dp[col] + dp[col + 1]
        return dp[0]


sol = Solution()
assert sol.uniquePaths(3, 7) == 28


# optimized
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        R = m
        C = n
        dp = [1] * C
        for _ in range(R-1):
            for col in range(C - 2, -1, -1):
                dp[col] = dp[col] + dp[col + 1]
        return dp[0]


sol = Solution2()
assert sol.uniquePaths(3, 7) == 28


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        R = m
        C = n
        memo = {}

        def dfs(row, col):
            if row == R - 1 and col == C - 1:
                return 1
            if row == R or col == C:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            path = dfs(row + 1, col) + dfs(row, col + 1)
            memo[(row, col)] = path
            return path

        return dfs(0, 0)


sol = Solution3()
assert sol.uniquePaths(3, 7) == 28
