#You are given an array of integers nums,
# there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# Return the max sliding window.
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length
from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    l, r = 0, 0
    deq = deque()
    res = []
    while r < len(nums):
        if r < k:
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)
            r += 1
        else:
            res.append(nums[deq[0]])
            while deq and deq[0] <= l:
                deq.popleft()
            while deq and nums[deq[-1]] <= nums[r]:
                deq.pop()
            deq.append(r)

            l += 1
            r += 1
    if deq:
        res.append(nums[deq[0]])
    return res


print(maxSlidingWindow([1,3,1,2,0,5], 3))
