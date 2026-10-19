# You are given a 0-indexed integer array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:
#
# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:
#
# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        lessThenTarget = 0
        targetCount = 0
        for n in nums:
            if n == target:
                targetCount += 1
            elif n < target:
                lessThenTarget += 1
        res = []
        for i in range(lessThenTarget, lessThenTarget + targetCount):
            res.append(i)
        return res


assert Solution().targetIndices([1,2,5,2,3], 2) == [1, 2]
assert Solution().targetIndices([1,2,5,2,3], 3) == [3]
