# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:
#
# Input: arr = [11,81,94,43,3]
# Output: 444
#
#
# Constraints:
#
# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = [-1]
        res = 0
        arr.append(0)
        for i, val in enumerate(arr):
            while stack and val < arr[stack[-1]]:
                index = stack.pop()
                left = index - stack[-1]
                right = i - index
                res += (right * left * arr[index]) % MOD
            stack.append(i)
        return res % MOD


sol = Solution()
assert sol.sumSubarrayMins([3,1,2,4]) == 17
