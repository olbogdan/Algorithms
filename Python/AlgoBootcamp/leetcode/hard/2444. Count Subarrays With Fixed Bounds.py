# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:
#
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# 1 <= nums[i], minK, maxK <= 106
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mi = ma = -1
        start = 0  # this is an index of a valid number, valid if in range (minK <= maxK)
        res = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                # cur num is invalid, move start to a next position
                mi = -1
                ma = -1
                start = i + 1
            else:
                # minK can be == to maxK, that is why we need two if blocks
                if num == minK:
                    mi = i
                if num == maxK:
                    ma = i

                if mi != -1 and ma != -1:
                    res += min(mi, ma) - start + 1
        return res


sol = Solution()
assert sol.countSubarrays([1,3,5,2,7,5], 1, 5) == 2
assert sol.countSubarrays([1,1,1,1], 1, 1) == 10
