# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        idxT = self.findT(nums, target)
        if idxT == -1:
            return [-1, -1]

        # second half

        secondHalfIdx = self.findT(nums, target, idxT + 1)
        secondIdxResult = secondHalfIdx
        while secondHalfIdx != -1:
            secondIdxResult = secondHalfIdx
            secondHalfIdx = self.findT(nums, target, secondIdxResult + 1)
        if secondIdxResult == -1:
            secondIdxResult = idxT

        # firstHalf
        firstHalfIdx = self.findT(nums, target, 0, idxT - 1)
        firstIdxResult = firstHalfIdx
        while firstHalfIdx != -1:
            firstIdxResult = firstHalfIdx
            firstHalfIdx = self.findT(nums, target, 0, firstIdxResult - 1)
        if firstIdxResult == -1:
            firstIdxResult = idxT

        return [firstIdxResult, secondIdxResult]

    def findT(self, nums: List[int], target: int, l: int = 0, r=None) -> int:
        if r is None:
            r = len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


