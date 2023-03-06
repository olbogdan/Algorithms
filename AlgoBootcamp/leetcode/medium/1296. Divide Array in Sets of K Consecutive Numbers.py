# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.
#
# Return true if it is possible. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Example 2:
#
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# Example 3:
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 109
from collections import Counter
from heapq import heappop, heapify
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        counter = Counter(nums)
        # stack should be at least size of k
        if len(counter.keys()) < k:
            return False

        h = list(counter.keys())
        heapify(h)

        while True:
            # shift the stack beginning pointer to nex available num
            while h and h[0] not in counter:
                heappop(h)
            if not h:
                return True
            for i in range(h[0], h[0] + k):
                if i in counter:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
                else:
                    return False


sol = Solution()
assert sol.isPossibleDivide([16,21,26,35], 4) is False
