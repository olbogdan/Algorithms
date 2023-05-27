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

# Intuition
# The difference from the 1st Shortest Subarray problem is in steps 1 and 3.
#
# Approach
# The difference from the 1st Shortest Subarray problem is step 1 and 3.
#
# Building a prefix sum in the first for loop.
# The first while loop works the same as in the 1st Shortest Subarray problem to narrow the queue from the left side.
# The second while loop is tricky, it narrows the queue from the right side. The main idea of the second while loop is to maintain an increasing sequence of prefix values in the deque. The deque is an array with indices that point to prefixes.
# Example:
#
# nums        [10,-2, 20]
# prefixes [0, 10, 8, 28]
# index     0  1   2  3
# k = 28
# Iterations of the for loop:
#
# i = 0
# deque is empty, both while loops are False
# add index 0 to the deque
# i = 1
# deque has one item [0]
# first while loop is False since:
# prefixes[i] - prefixes[queue[0]] -> 10 - 0 >= k(28) is False.
# second while is False since: prefixes[i] <= prefixes[queue[-1]] -> 10 <= 0 is False
# add index 1 to the deque.
# i = 2
# deque [0, 1]
# prefixes [0, 10]
# first while is False 8 - 0 >= 28
# second wile is True 8 <= 10 THIS IS IMPORTANT, we have to remove the last index from the deque to maintain an increasing subarray. Else we would have [0, 10, 8] but we want to have [0, 8].
# add 2 to the deque.
# i = 3
# deque [0, 2]
# prefixes [0, 8]
# first while loop is True 28 - 0 >= 28 this is our resul. We are removing left index fro deque (aka left pointer) to check if smaller window will be valid.
# second while loop is false since 28 makes an increasing subarray with 0 and 8 [0, 8, 28].
# Complexity
# Time complexity:
# O(n)
#
# Space complexity:
# O(n)


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
