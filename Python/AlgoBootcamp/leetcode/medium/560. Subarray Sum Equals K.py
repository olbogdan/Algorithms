# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # memoize how many times each sum was repeated
        # deduct from a sum k
        # search the difference in memorized prefixes, increase result on amount of reps
        # [1, 1, 2, 1] (3)
        # memo[1] = 1 (calc 1-3 = -2, memo[-2] does not exist)
        # memo[2(1+1)] = 1 (calc 2-3 = -1, momo[-1] does not exist)
        # memo[4(1+1+2)] = 1 & (cal 4-3 = 1, memo[1] is 1, increment res by 1)
        # memo[5(1+1+2+1)] = 1 & (calc 5-3 = 2, memo[2] is 1, increment res by 1)
        memo = {}
        # special base case, will be triggered when sum - k == 0, means sum equals to k
        memo[0] = 1
        result = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum - k in memo:
                result += memo[curSum - k]
            if curSum not in memo:
                memo[curSum] = 1
            else:
                memo[curSum] = memo[curSum] + 1
        return result


sol = Solution()
assert sol.subarraySum([1,1,1], 2) == 2
assert sol.subarraySum([1,2,3], 3) == 2
