# You are given an integer array nums.
#
# Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.
#
# After that, you repeat the following process:
#
# If curr is out of the range [0, n - 1], this process ends.
# If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
# Else if nums[curr] > 0:
# Decrement nums[curr] by 1.
# Reverse your movement direction (left becomes right and vice versa).
# Take a step in your new direction.
# A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.
#
# Return the number of possible valid selections.
#
#
#
# Example 1:
#
# Input: nums = [1,0,2,0,3]
#
# Output: 2
#
# Explanation:
#
# The only possible valid selections are the following:
#
# Choose curr = 3, and a movement direction to the left.
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
# Choose curr = 3, and a movement direction to the right.
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].
# Example 2:
#
# Input: nums = [2,3,4,0,4,1,0]
#
# Output: 0
#
# Explanation:
#
# There are no possible valid selections.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# There is at least one element i where nums[i] == 0.
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        pre, suf = [0] * N, [0] * N

        for i in range(1, N):
            pre[i] = pre[i - 1] + nums[i - 1]

        for i in range(N - 2, -1, -1):
            suf[i] = suf[i + 1] + nums[i + 1]

        res = 0
        for i, v in enumerate(nums):
            if v != 0:
                continue
            diff = abs(pre[i] - suf[i])
            res += 2 if diff == 0 else (1 if diff == 1 else 0)
        return res


sol = Solution()
assert sol.countValidSelections([1, 0, 2, 0, 3]) == 2
assert sol.countValidSelections([2, 3, 4, 0, 4, 1, 0]) == 0
