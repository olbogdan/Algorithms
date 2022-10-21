# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
# of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique
# if the frequency of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum up to target is less
# than 150 combinations for the given input.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
#
# Input: candidates = [2], target = 1
# Output: []
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
from collections import deque
from typing import List


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        tempResult = deque()
        def dfs(i, sumOfNums):
            if sumOfNums == target:
                result.append(list(tempResult))
            elif sumOfNums < target and i < len(candidates):
                tempResult.append(candidates[i])
                dfs(i, candidates[i] + sumOfNums)
                tempResult.pop()
                dfs(i+1, sumOfNums)
        dfs(0, 0)
        return result


solution = Solution1()
assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert solution.combinationSum([2], 1) == []


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        tempResult = []
        def dfs(nums, sumOfNums):
            if sumOfNums == target:
                result.append(tempResult.copy())
            elif sumOfNums < target and len(nums) > 0:
                tempResult.append(nums[-1])
                dfs(nums, nums[-1] + sumOfNums)
                tempResult.pop()
                temp = nums.pop()
                dfs(nums, sumOfNums)
                nums.append(temp)
        dfs(candidates, 0)
        return list(result)


solution = Solution2()
assert solution.combinationSum([2, 3, 6, 7], 7) == [[7], [3, 2, 2]]
assert solution.combinationSum([2, 3, 5], 8) == [[5, 3], [3, 3, 2], [2, 2, 2, 2]]
assert solution.combinationSum([2], 1) == []