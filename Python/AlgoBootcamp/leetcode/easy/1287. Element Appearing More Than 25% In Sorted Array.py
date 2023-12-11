# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
#
#
#
# Example 1:
#
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:
#
# Input: arr = [1,1]
# Output: 1
#
#
# Constraints:
#
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num = arr[0]
        reps = 1
        quarter = len(arr) / 4
        for i in range(1, len(arr)):
            if num == arr[i]:
                reps += 1
            else:
                num = arr[i]
                reps = 1

            if quarter < reps:
                return num
        return num


sol = Solution()
assert sol.findSpecialInteger([1,1,2,2,3,3,3,3]) == 3
