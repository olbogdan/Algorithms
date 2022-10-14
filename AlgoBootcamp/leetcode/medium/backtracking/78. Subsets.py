# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    currentSubset = []

    def dfs(start):
        if start == len(nums):
            result.append(currentSubset.copy())
            return
        currentSubset.append(nums[start])
        dfs(start + 1)
        currentSubset.pop()
        dfs(start + 1)

    dfs(0)
    return result


assert subsets([1,2,3]) == [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]
assert subsets([0]) == [[0],[]]


