# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
#
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
#
# Note that abs(x) is defined as follows:
#
# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
#
#
# Example 1:
#
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# Example 2:
#
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maximize = minimize = res = 0
        for n in nums:
            maximize += n
            if maximize < 0:
                maximize = 0
            minimize += n
            if minimize > 0:
                minimize = 0
            res = max(res, maximize, abs(minimize))

        return res


sol = Solution()
assert sol.maxAbsoluteSum([1,-3,2,3,-4]) == 5
assert sol.maxAbsoluteSum([2,-5,1,-4,3,-2]) == 8
