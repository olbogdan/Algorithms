# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists, then return its index.
# Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


assert search([-1,0,3,5,9,12], 9) == 4
assert search([2,5], 0) == -1
assert search([-1,0,3,5,9,12], 2) == -1
assert search([-1,0,3,5,9,12], 13) == -1


def searchRec(nums: List[int], target: int) -> int:
    def bsr(left, right):
        if left > right:
            return -1
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) // 2
        if nums[mid] < target:
            return bsr(mid + 1, right)
        elif nums[mid] > target:
            return bsr(left, mid - 1)
        else:
            return mid
    return bsr(0, len(nums) - 1)


assert searchRec([-1,0,3,5,9,12], 9) == 4
assert searchRec([2,5], 0) == -1
assert searchRec([-1,0,3,5,9,12], 2) == -1
assert searchRec([-1,0,3,5,9,12], 13) == -1

