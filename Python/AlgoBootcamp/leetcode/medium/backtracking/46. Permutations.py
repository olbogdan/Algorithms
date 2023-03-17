# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []

        def dfs(leftBorder):
            if leftBorder == len(nums):
                res.append(prem[:])
                return
            for i in range(leftBorder, len(nums)):
                prem.append(nums[i])

                nums[leftBorder], nums[i] = nums[i], nums[leftBorder]
                dfs(leftBorder + 1)
                nums[leftBorder], nums[i] = nums[i], nums[leftBorder]

                prem.pop()

        dfs(0)
        return res


sol = Solution()
assert sol.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
