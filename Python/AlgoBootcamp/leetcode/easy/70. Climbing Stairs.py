# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
#
# 1 <= n <= 45


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        for _ in range(n - 2):
            first, second = second, first + second
        return second


sol = Solution()
assert sol.climbStairs(3) == 3
assert sol.climbStairs(4) == 5
assert sol.climbStairs(10) == 89
assert sol.climbStairs(1) == 1


class Solution2:
    def climbStairs(self, n: int) -> int:
        cur = 1
        prev = 1
        for i in range(n-1):
            newVal = cur + prev
            prev = cur
            cur = newVal
        return cur


sol = Solution2()
assert sol.climbStairs(3) == 3
assert sol.climbStairs(4) == 5
assert sol.climbStairs(10) == 89
assert sol.climbStairs(1) == 1


class Solution2:
    def climbStairs(self, n: int) -> int:
        arr = [1]*(n+1)
        for i in range(n-1, -1, -1):
            step = i + 1
            twoSteps = i + 2
            reachability = 0
            if step < len(arr):
                reachability += arr[step]
            if twoSteps < len(arr):
                reachability += arr[twoSteps]
            arr[i] = reachability
        return arr[0]


sol = Solution2()
assert sol.climbStairs(3) == 3
assert sol.climbStairs(4) == 5
assert sol.climbStairs(10) == 89
assert sol.climbStairs(1) == 1


class Solution3:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            if i in memo:
                return memo[i]

            rep = dfs(i + 1) + dfs(i + 2)
            memo[i] = rep
            return rep

        return dfs(0)


sol = Solution3()
print(sol.climbStairs(4))
