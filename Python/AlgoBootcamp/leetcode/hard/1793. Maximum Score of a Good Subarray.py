# You are given an array of integers nums (0-indexed) and an integer k.
#
# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
#
# Return the maximum possible score of a good subarray.
#
#
#
# Example 1:
#
# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
# Example 2:
#
# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 2 * 104
# 0 <= k < nums.length
from cmath import inf
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        result = nums[k]
        minNumber = nums[k]
        N = len(nums)
        # while we can take left+1 or right+1
        while l > 0 or r < N-1:
            left = float(-inf)
            if l-1 >= 0:
                left = nums[l-1]
            right = float(-inf)
            if r < N - 1:
                right = nums[r+1]

            # at least one or right or left is bigger then float(-inf)
            # take the biggest of two sides
            if left > right:
                minNumber = min(minNumber, left)
                l -= 1
            else:
                minNumber = min(minNumber, right)
                r += 1
            distance = r - l + 1
            result = max(result, minNumber * distance)
        return result


sol = Solution()
res = sol.maximumScore([5,5,4,5,4,1,1,1], 0)
assert res == 20

res = sol.maximumScore([1,4,3,7,4,5], 3)
assert res == 15
