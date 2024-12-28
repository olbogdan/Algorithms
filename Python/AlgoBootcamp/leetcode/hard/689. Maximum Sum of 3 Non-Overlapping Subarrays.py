# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Example 2:
#
# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4]
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prSum = [sum(nums[:k])]
        for i in range(k, len(nums)):
            prSum.append(prSum[-1] - nums[i-k] + nums[i])
        memo = {}
        def dp(i, cnt):
            if cnt == 3 or i > len(nums) - k:
                return 0
            if (i, cnt) in memo:
                return memo[(i, cnt)]
            include = dp(i+k, cnt+1) + prSum[i]
            skip = dp(i+1, cnt)
            localRes = max(include, skip)
            memo[(i, cnt)] = localRes
            return localRes
        res = []
        i = 0
        while i <= len(nums)-k and len(res) < 3:
            include = dp(i+k, len(res)+1) + prSum[i]
            skip = dp(i+1, len(res))
            if include >= skip:
                res.append(i)
                i += k
            else:
                i += 1
        return res


sol = Solution()
sol.maxSumOfThreeSubarrays([1,2,1,2,2,2,2,2], 2) == [0, 3, 5]
sol.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2) == [0, 2, 4]
sol.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2) == [0, 3, 5]
