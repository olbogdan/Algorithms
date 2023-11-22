# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
#
#
#
# Example 1:
#
#
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# Example 2:
#
#
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i].length <= 105
# 1 <= sum(nums[i].length) <= 105
# 1 <= nums[i][j] <= 105
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        numMap = defaultdict(list)
        n = 0
        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                weight = r + c
                n = max(n, weight)
                numMap[weight].append(nums[r][c])
        result = []
        for i in range(n + 1):
            for num in numMap[i]:
                result.append(num)
        return result


sol = Solution()
assert sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]) == [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]


class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        numList = []
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                weight = r + c
                numList.append((weight, c, nums[r][c]))
        numList.sort()
        result = []
        for _, _, num in numList:
            result.append(num)
        return result


