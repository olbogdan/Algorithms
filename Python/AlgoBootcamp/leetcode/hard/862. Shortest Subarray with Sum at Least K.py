# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1], k = 1
# Output: 1
# Example 2:
#
# Input: nums = [1,2], k = 4
# Output: -1
# Example 3:
#
# Input: nums = [2,-1,2], k = 3
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 109
import collections
from cmath import inf
from typing import List


class Solution1:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefixes = [0] * (N + 1)
        for i in range(1, N + 1):
            prefixes[i] = nums[i - 1] + prefixes[i - 1]

        res = float(inf)
        queue = collections.deque()
        for i in range(len(prefixes)):
            while queue and prefixes[i] - prefixes[queue[0]] >= k:
                res = min(res, i - queue.popleft())

            while queue and prefixes[i] <= prefixes[queue[-1]]:
                queue.pop()

            queue.append(i)
        return -1 if res == float(inf) else res


sol = Solution1()
res1 = sol.shortestSubarray([2, -1, 2], 3)
assert res1 == 3


class Solution2:
    def shortestSubarray(self, nums, k):
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(nums):
            cur += a
            while d and cur - d[0][1] >= k:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
