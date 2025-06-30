# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
#
#
#
# Example 1:
#
# Input: nums = [1,3,2,2,5,2,3,7]
#
# Output: 5
#
# Explanation:
#
# The longest harmonious subsequence is [3,2,2,2,3].
#
# Example 2:
#
# Input: nums = [1,2,3,4]
#
# Output: 2
#
# Explanation:
#
# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.
#
# Example 3:
#
# Input: nums = [1,1,1,1]
#
# Output: 0
#
# Explanation:
#
# No harmonic subsequence exists.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109
from typing import List, Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        sortedKeys = sorted(count.keys())
        res = 0
        for i in range(1, len(sortedKeys)):
            if sortedKeys[i] - sortedKeys[i - 1] == 1:
                res = max(res, count[sortedKeys[i]] + count[sortedKeys[i - 1]])
        return res


sol = Solution()
assert sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
assert sol.findLHS([1, 2, 3, 4]) == 2
