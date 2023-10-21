# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
#
# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
#
#
#
# Example 1:
#
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# Example 2:
#
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.
# Example 3:
#
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
from heapq import heappush, heappop
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = []
        heappush(heap, [-nums[0], 0]) # decreasing heap [value, index]
        result = nums[0]
        for i in range(1, len(nums)):
            while heap and i - heap[0][1] > k:
                heappop(heap)
            prevMax = -heap[0][0]
            curMax = max(nums[i], prevMax + nums[i])
            result = max(result, curMax)
            heappush(heap, [-curMax, i])

        return result


sol = Solution()
assert sol.constrainedSubsetSum([10,-2,-10,-5,20], 2) == 23
