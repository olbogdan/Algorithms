# You are given an integer array nums.
#
# You replace each element in nums with the sum of its digits.
#
# Return the minimum element in nums after all replacements.
#
#
#
# Example 1:
#
# Input: nums = [10,12,13,14]
#
# Output: 1
#
# Explanation:
#
# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.
#
# Example 2:
#
# Input: nums = [1,2,3,4]
#
# Output: 1
#
# Explanation:
#
# nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.
#
# Example 3:
#
# Input: nums = [999,19,199]
#
# Output: 10
#
# Explanation:
#
# nums becomes [27, 10, 19] after all replacements, with minimum element 10.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 104
from cmath import inf
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float(inf)
        for num in nums:
            strNum = str(num)
            candidate = 0
            for dj in range(len(strNum)):
                candidate += int(strNum[dj])
            res = min(res, candidate)
        return res


sol = Solution()
assert sol.minElement([10,12,13,14]) == 1
assert sol.minElement([1,2,3,4]) == 1