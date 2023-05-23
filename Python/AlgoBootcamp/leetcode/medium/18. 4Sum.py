# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        N = len(nums)

        for i1 in range(N - 3):
            # skip duplicates
            if i1 >= 1 and nums[i1] == nums[i1 - 1]:
                continue

            for i2 in range(i1 + 1, N - 2):
                if i2 >= i1 + 2 and nums[i2] == nums[i2 - 1]:
                    continue

                # [L1, 2, 3, R4]
                # solve 2 sum sorted problem
                L = i2 + 1
                R = N - 1
                while L < R:
                    nSum = nums[i1] + nums[i2] + nums[L] + nums[R]
                    if nSum < target:
                        L += 1
                    elif nSum > target:
                        R -= 1
                    else:
                        result.append([nums[i1], nums[i2], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        # skip duplicates
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
        return result


sol = Solution()
res = sol.fourSum([-1,0,0,1,2], 0)
assert res == [[-1, 0, 0, 1]]
res = sol.fourSum([2,2,2,2,2], 8)
assert res == [[2, 2, 2, 2]]
