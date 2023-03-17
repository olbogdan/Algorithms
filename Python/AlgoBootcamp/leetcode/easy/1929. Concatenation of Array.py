# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


sol = Solution()
assert sol.getConcatenation([1,2,3]) == [1,2,3,1,2,3]


class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums*2)
        for i in range(2):
            for j in range(len(nums)):
                level = 0
                if i > 0:
                    level += len(nums) * i
                res[j+level] = nums[j]
        return res


sol = Solution2()
assert sol.getConcatenation([1,2,3]) == [1,2,3,1,2,3]
