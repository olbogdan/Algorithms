# 1802. Maximum Value at a Given Index in a Bounded Array
# Medium
# 1.7K
# 274
# Companies
# You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:
#
# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.
#
# Note that abs(x) equals x if x >= 0, and -x otherwise.
#
#
#
# Example 1:
#
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
# Example 2:
#
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= maxSum <= 109
# 0 <= index < n


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calcSum(cnt, end):
            if cnt == 0:
                return 0
            start = max(end - cnt, 0)
            sum1 = end * (1 + end) // 2
            sum2 = start * (1 + start) // 2
            return sum1 - sum2

        maxSum -= n
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            leftSum = calcSum(index + 1, mid)
            rightSum = calcSum(n - index - 1, mid - 1)
            if leftSum + rightSum <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return l


sol = Solution()
res = sol.maxValue(4, 2, 6)
assert res == 2
res = sol.maxValue(6, 1, 10)
assert res == 3
res = sol.maxValue(1, 0, 6)
assert res == 6