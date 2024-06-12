# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        reps = 0
        for n in nums:
            if res == n:
                reps += 1
            elif reps == 0:
                res = n
                reps += 1
            else:
                reps -= 1
        return res


sol = Solution()
assert sol.majorityElement([2,2,1,1,1,2,2]) == 2


class Count:
    def __init__(self, num, repeat):
        self.num = num
        self.repeat = repeat


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Count(nums[0], 1)
        for i in range(1, len(nums)):
            if counter.num == nums[i]:
                counter.repeat += 1
            else:
                counter.repeat -= 1

                if counter.repeat == 0:
                    counter = Count(nums[i], 1)
        return counter.num


sol = Solution2()
assert sol.majorityElement([2,2,1,1,1,2,2]) == 2
