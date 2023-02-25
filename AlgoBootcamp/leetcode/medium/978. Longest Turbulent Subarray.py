# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
#
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
#
# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
#
#
# Example 1:
#
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:
#
# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:
#
# Input: arr = [100]
# Output: 1
#
#
# Constraints:
#
# 1 <= arr.length <= 4 * 104
# 0 <= arr[i] <= 109
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1
        prev = ""
        result = 1
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                result = max(result, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                result = max(result, r - l + 1)
                r += 1
                prev = "<"
            else:
                if arr[r-1] == arr[r]:
                    l = r
                    r += 1
                else:
                    l = r-1
                prev = ""

        return result


sol = Solution()
assert sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
assert sol.maxTurbulenceSize([4,8,12,16]) == 2
assert sol.maxTurbulenceSize([16]) == 1
