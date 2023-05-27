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


class Solution:
    # def shortestSubarray(self, nums, k):
        # d = collections.deque([[0, 0]])
        # res, cur = float('inf'), 0
        # for i, a in enumerate(nums):
        #     cur += a
        #     while d and cur - d[0][1] >= k:
        #         res = min(res, i + 1 - d.popleft()[0])
        #     while d and cur <= d[-1][1]:
        #         d.pop()
        #     d.append([i + 1, cur])
        # return res if res < float('inf') else -1
    def shortestSubarray(self, A, K):
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N):
            B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in range(N + 1):
            while d and B[i] - B[d[0]] >= K: #[0, 10(TRUE), 120T, 1120b[d0], 920(FALSE)]
                res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]: # True only if negative val or 0
                d.pop()
            d.append(i)
        return res if res <= N else -1


sol = Solution()
res1 = sol.shortestSubarray([2,-1,2], 3)
assert res1 == 3
