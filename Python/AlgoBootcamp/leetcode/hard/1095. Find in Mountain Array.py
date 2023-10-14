# You may recall that an array arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.
#
# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
#
# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
#
#
#
# Example 1:
#
# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:
#
# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
#
#
# Constraints:
#
# 3 <= mountain_arr.length() <= 104
# 0 <= target <= 109
# 0 <= mountain_arr.get(index) <= 109


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, mockArray = []):
        self.arr = mockArray

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.arr):
            return None
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 10**4 is 10000 so that we need to find the result in one path
        # Log2 from 10000 -> 13, restriction: max 100 calls,
        # simpler solution will be to find a pick and search on half
        pick = self.findPick(mountain_arr)

        targetIdx = self.findInIncreasingArr(target, mountain_arr, pick)
        if targetIdx >= 0:
            return targetIdx
        return self.findInDecreasingArr(target, mountain_arr, pick)

    def findInIncreasingArr(self, target: int, arr: 'MountainArray', pick: int) -> int:
        l = 0
        r = pick
        while l <= r:
            mid = l + (r - l) // 2
            medium = arr.get(mid)
            if medium == target:
                return mid
            elif medium < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def findInDecreasingArr(self, target: int, arr: 'MountainArray', pick: int) -> int:
        l = pick
        r = arr.length() - 1
        while l <= r:
            mid = l + (r - l) // 2
            medium = arr.get(mid)
            if medium == target:
                return mid
            elif medium < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def findPick(self, arr: 'MountainArray') -> int:
        N = arr.length()
        l = 0
        r = N - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0:
                l += 1
                continue
            if mid == N - 1:
                r -= 1
                continue
            left = arr.get(mid - 1)
            medium = arr.get(mid)
            right = arr.get(mid + 1)

            if left < medium > right:
                return mid
            elif left < medium:
                l = mid + 1
            else:
                r = mid - 1
        return -1


mock = MountainArray([1,2,3,4,5,3,1])
sol = Solution()
res = sol.findInMountainArray(4, mock)
assert res == 3

mock = MountainArray([3,5,3,2,0])
sol = Solution()
res = sol.findInMountainArray(0, mock)
assert res == 4
