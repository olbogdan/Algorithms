# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
#
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:
#
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# All the integers in nums are unique.
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        maxSize, maxIndex = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > maxSize:
                        maxSize = dp[i]
                        maxIndex = i

        result = []
        num = nums[maxIndex]
        for i in range(maxIndex, -1, -1):
            if num % nums[i] == 0 and dp[i] == maxSize:
                result.append(nums[i])
                num = nums[i]
                maxSize -= 1

        return result


sol = Solution()
assert sol.largestDivisibleSubset([1,2,3]) == [2,1]
