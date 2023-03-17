# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
from random import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2, target):
            i = a1 = a2 = 0
            while a1 < len(arr1) and a2 < len(arr2):
                if arr1[a1] < arr2[a2]:
                    target[i] = arr1[a1]
                    a1 += 1
                else:
                    target[i] = arr2[a2]
                    a2 += 1
                i += 1

            while a1 < len(arr1):
                target[i] = arr1[a1]
                a1 += 1
                i += 1
            while a2 < len(arr2):
                target[i] = arr2[a2]
                a2 += 1
                i += 1

            return target

        def sort(arr):
            if len(arr) < 2:
                return arr
            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            return merge(left, right, arr)

        return sort(nums)


class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        # quick sort
        # take a pivot, move all smaller left and all greater right
        # repeat the same process on half until half has 1 or 0

        def qs(low, high):
            if low < high:
                pivot_index = partition(low, high)
                qs(low, pivot_index - 1)
                qs(pivot_index + 1, high)

        def partition(low, high):
            pivot = arr[high]
            i = low

            for j in range(low, high):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[high] = arr[high], arr[i]
            return i

        qs(0, len(arr)-1)
        return arr


sol = Solution()
res = sol.sortArray([5,1,1,2,0,0])
assert res == [0, 0, 1, 1, 2, 5]
res = sol.sortArray([2,2,0,1])
assert res == [0, 1, 2, 2]


class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:

        def qs(low, high):
            if low >= high:
                return
            pivot = nums[random.randint(low, high)]
            left = low
            mid = low
            right = high

            while mid <= right:
                if nums[mid] < pivot:
                    nums[mid], nums[left] = nums[left], nums[mid]
                    left += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[right] = nums[right], nums[mid]
                    right -= 1
                else:
                    mid += 1

            qs(low, left-1)
            qs(right+1, high)

        qs(0, len(nums)-1)
        return nums
