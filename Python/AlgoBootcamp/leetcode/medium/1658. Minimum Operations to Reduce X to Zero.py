# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
#
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
#
#
#
# Example 1:
#
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:
#
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:
#
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109
from cmath import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        total = sum(nums)
        l = 0
        r = 0
        subSum = 0
        result = float(inf)
        while True:
            remaining = total - subSum
            if remaining == x:
                result = min(result, N - (r - l))
                # optimisation
                if result == 1:
                    break

            if remaining >= x or l == r:
                if r >= N:
                    break
                subSum += nums[r]
                r += 1
                continue
            if remaining < x:
                if l >= N:
                    break
                subSum -= nums[l]
                l += 1
                continue
        return result if result != float(inf) else -1


sol = Solution()
res = sol.minOperations([1,1,4,2,3], 5)
assert res == 2
res = sol.minOperations([5,6,7,8,9], 4)
assert res == -1
res = sol.minOperations([8576], 8576)
assert res == 1
res = sol.minOperations([8575], 8576)
assert res == -1
