# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
#
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
#
#
#
# Example 1:
#
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]
# Example 2:
#
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.
#
#
# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?
from typing import List


class Solution1:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        return res


sol = Solution1()
assert sol.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]


class Solution2:
    def buildArray(self, nums: List[int]) -> List[int]:
        def dfs(i):
            if nums[i] < 0:
                return nums[i]
            if nums[i] == i:
                if nums[i] > 0:
                    nums[i] = -nums[i]
                else:
                    nums[i] = float('-inf')
                return None
            nextI = nums[i]
            nums[i] = -nums[i]
            nums[i] = dfs(nextI)
            return -nextI

        for i in range(len(nums)):
            if nums[i] >= 0:
                dfs(nums[i])
        for i in range(len(nums)):
            if nums[i] == float('-inf'):
                nums[i] = 0
            if nums[i] < 0:
                nums[i] = -nums[i]
        return nums


sol = Solution2()
assert sol.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]
