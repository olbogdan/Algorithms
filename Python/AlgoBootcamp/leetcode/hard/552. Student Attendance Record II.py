# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
#
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
# Example 2:
#
# Input: n = 1
# Output: 3
# Example 3:
#
# Input: n = 10101
# Output: 183236316
#
#
# Constraints:
#
# 1 <= n <= 105


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = []
        for _ in range(n+1):
            memo.append([[-1]*2 for _ in range(3)])

        def dp(n, absent, late):
            if absent > 1 or late > 2:
                return 0
            if n == 0:
                return 1
            if memo[n][late][absent] != -1:
                return memo[n][late][absent]
            # Present
            res = dp(n-1, absent, 0) % MOD
            # Absent
            res = (res + dp(n-1, absent + 1, 0)) % MOD
            # Late
            res = (res + dp(n-1, absent, late+1)) % MOD
            memo[n][late][absent] = res
            return res

        return dp(n, 0, 0)



sol = Solution()
assert sol.checkRecord(2) == 8
assert sol.checkRecord(1) == 3
