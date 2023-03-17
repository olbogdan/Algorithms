# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
# You are also given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and
# the lowest of the k scores is minimized.
#
# Return the minimum possible difference.
# Example 1:
#
# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Example 2:
#
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.
from math import inf
from typing import List


def minimumDifference(nums: List[int], k: int) -> int:
    if not nums or len(nums) == 1:
        return 0
    nums.sort()
    l, r = 0, k - 1
    minDiff = float(inf)
    while r < len(nums):
        minDiff = min(minDiff, nums[r] - nums[l])
        l += 1
        r += 1
    return minDiff


assert minimumDifference([20980,13353,51423,11920,41836,51586,54445], 5) == 33465
assert minimumDifference([90], 1) == 0
assert minimumDifference([9,4,1,7], 2) == 2
assert minimumDifference([1,22,23,50], 2) == 1
assert minimumDifference([1,22,23,50], 1) == 0
