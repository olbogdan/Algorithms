# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
# Example 1:
#
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
#
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # let's allocate sliding window
        # move right while arr[R + 1] is closer to x then L
        L = 0
        R = k - 1
        while R < len(arr) - 1:
            leftDistance = abs(x - arr[L])
            rightDistance = abs(x - arr[R + 1])
            # To handle duplicate values do a check L != R: [1L,1R,1,10,10,10] k 1, x 9
            if arr[L] != arr[R + 1] and leftDistance <= rightDistance:
                return arr[L:(R + 1)]
            R += 1
            L += 1
        return arr[L:(R + 1)]


sol = Solution()
assert sol.findClosestElements([1,1,1,10,10,10], 1, 9) == [10]
assert sol.findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4]
