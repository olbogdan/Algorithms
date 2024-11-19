# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
#
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:
#
# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 105
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        window = set()
        curSum = 0
        l = 0
        for r in range(N):
            if nums[r] not in window:
                window.add(nums[r])
                curSum += nums[r]
                if len(window) == k:
                    res = max(res, curSum)
                    curSum -= nums[l]
                    window.remove(nums[l])
                    l += 1
            else:
                while nums[l] != nums[r]:
                    window.remove(nums[l])
                    curSum -= nums[l]
                    l += 1
                l += 1
        return res


sol = Solution()
assert sol.maximumSubarraySum([1,5,4,2,9,9,9], 3) == 15
assert sol.maximumSubarraySum([4,4,4], 3) == 0
