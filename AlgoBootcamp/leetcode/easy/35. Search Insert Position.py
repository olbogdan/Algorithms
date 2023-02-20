# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,8,9] t= 5
        # [1,3R,8L,9]
        # [1,3,10] t = 5
        # [1,3R,10L]
        # [1,3,10] t = 2
        # [1R,3L,10]
        # [1,3,8,9] t=0
        # -1R[1L,3,8,9]
        # [1,3,8,9] t=20
        # [1,3,8,9R]10L
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l


sol = Solution()
assert sol.searchInsert([1,3,5,6], 2) == 1
assert sol.searchInsert([1,3,5,6], 7) == 4
