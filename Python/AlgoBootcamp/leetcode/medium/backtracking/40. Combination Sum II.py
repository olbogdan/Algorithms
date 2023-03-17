# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
# Constraints:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combi = []
        candidates.sort()

        def dfs(i, sumOfNums):
            if sumOfNums == target:
                result.append(combi[:])
                return
            if sumOfNums > target or i >= len(candidates):
                return

            combi.append(candidates[i])
            dfs(i + 1, sumOfNums + candidates[i])

            combi.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, sumOfNums)

        dfs(0, 0)
        return result


sol = Solution()
assert sol.combinationSum2([2,5,2,1,2], 5) == [[1, 2, 2], [5]]
assert sol.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27) == []
