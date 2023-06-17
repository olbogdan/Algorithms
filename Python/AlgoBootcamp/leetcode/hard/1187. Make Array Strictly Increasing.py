# Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
#
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
#
# If there is no way to make arr1 strictly increasing, return -1.
#
#
#
# Example 1:
#
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
# Example 2:
#
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
# Example 3:
#
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# Explanation: You can't make arr1 strictly increasing.
#
#
# Constraints:
#
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
from cmath import inf
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2 = sorted(list(set(arr2)))

        cache = {}

        def dp(i, j, prevVal):
            if i == len(arr1):
                return 0

            if (i, prevVal) in cache:
                return cache[(i, prevVal)]

            while j < len(arr2) and prevVal >= arr2[j]:
                j += 1
                # j is bigger than previous or out of bounds

            result = inf

            if prevVal < arr1[i]:
                result = dp(i + 1, j, arr1[i])

            if j < len(arr2):
                result = min(result, 1 + dp(i + 1, j, arr2[j]))

            cache[(i, prevVal)] = result
            return result

        result = dp(0, 0, float(-inf))
        return -1 if result == inf else result


sol = Solution()
res = sol.makeArrayIncreasing([13,2,17,2,1,8,7,10,3,12,7,20,13], [25,16,17,10,25,18,13,8,3,22,1,20,13,18,25,20,11,18,15,12])
assert res == 11
res = sol.makeArrayIncreasing([0,11,6,1,4,3], [5,4,11,10,1,0])
assert res == 5
res = sol.makeArrayIncreasing([1,5,3,6,7], [4,3,1])
assert res == 2
