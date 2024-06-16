# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
#
# Return the minimum number of patches required.
#
#
#
# Example 1:
#
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# Example 2:
#
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
# Example 3:
#
# Input: nums = [1,2,2], n = 5
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# nums is sorted in ascending order.
# 1 <= n <= 231 - 1
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # observations:
        # ideal sequance 1,2,4,8,16
        # but in this task we need to operate on sum instead of prev good number
        # to get a next good number based on sum take SUM + 1 - it is a next candidate
        # add this number to a curent SUM

        patches = 0
        i = 0

        # This represents the maximum sum we can achieve with the current array and patches
        coveredSum = 0

        while coveredSum < n:
            # example: covered sum is 3 {range 1:3 covered} next optimal 4
            nextOptimalValue = coveredSum + 1
            # we don't always need to take an optimal next number, nums array has priority
            # since we don't use patches when we take an item from the array
            if i < len(nums) and nums[i] <= nextOptimalValue:
                # If the current number can extend the covered range, use it
                coveredSum += nums[i]
                i += 1
            else:
                # Otherwise, add a patch to extend the covered range
                coveredSum += nextOptimalValue
                patches += 1

        return patches


sol = Solution()
assert sol.minPatches([1,2,31,33], 2147483647) == 28
assert sol.minPatches([1, 3], 6) == 1
