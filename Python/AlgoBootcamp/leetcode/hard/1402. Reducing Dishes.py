# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
#
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
#
# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
#
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
#
#
#
# Example 1:
#
# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.
# Example 2:
#
# Input: satisfaction = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
# Example 3:
#
# Input: satisfaction = [-1,-4,-5]
# Output: 0
# Explanation: People do not like the dishes. No dish is prepared.
#
#
# Constraints:
#
# n == satisfaction.length
# 1 <= n <= 500
# -1000 <= satisfaction[i] <= 1000


from functools import cache
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @cache
        def dfs(idx, time):
            if idx >= len(satisfaction):
                return 0
            # take this and next
            this = satisfaction[idx] * time + dfs(idx + 1, time + 1)

            # take only next
            takeOnlyNext = dfs(idx + 1, time)

            return max(this, takeOnlyNext)

        return dfs(0, 1)


sol = Solution()
res = sol.maxSatisfaction([4,3,2])
assert res == 20


class Solution2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        def dfs(idx, time):
            if idx >= len(satisfaction):
                return 0
            # [-1, -3, 100] after sort:
            # [-3, -1, 100]
            # -3*0 0 + -1*1 -1 + 100*2
            # take cur and next
            # take cur and no next
            this = satisfaction[idx] * time
            nextVal = dfs(idx + 1, time + 1)
            return max(this + nextVal, this)

        res = 0
        for i in range(len(satisfaction)):
            res = max(res, dfs(i, 1))
        return res


sol = Solution2()
res = sol.maxSatisfaction([4,3,2])
assert res == 20
