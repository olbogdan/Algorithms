# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
#
#
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        mid = 0
        for i in range(N):
            if nums[i] < 0:
                mid = i
            nums[i] = nums[i] ** 2
        result = []
        left = mid
        right = mid + 1
        while left >= 0 or right < N:
            if left < 0:
                result.append(nums[right])
                right += 1
                continue
            if right == N:
                result.append(nums[left])
                left -= 1
                continue
            if nums[left] < nums[right]:
                result.append(nums[left])
                left -= 1
            else:
                result.append(nums[right])
                right += 1

        return result


sol = Solution()
assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
