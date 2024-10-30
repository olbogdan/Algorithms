# You may recall that an array arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove any elements.
# Example 2:
#
# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
#
#
# Constraints:
#
# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# It is guaranteed that you can make a mountain array out of nums.
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        increasing = self.calculateIncreas(nums)
        decreasing = list(reversed(self.calculateIncreas(list(reversed(nums)))))
        res = N
        for i in range(1, N - 1):
            dec = decreasing[i]
            inc = increasing[i]
            if inc > 1 and dec > 1:
                res = min(res, N - dec - inc + 1)
        return res

    def calculateIncreas(self, nums: List[int]) -> List[int]:
        N = len(nums)
        increasing = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    increasing[i] = max(increasing[i], increasing[j] + 1)
        return increasing


sol = Solution()
assert sol.minimumMountainRemovals([1,3,1]) == 0
assert sol.minimumMountainRemovals([2,1,1,5,6,2,3,1]) == 3
