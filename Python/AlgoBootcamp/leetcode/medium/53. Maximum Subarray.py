# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.

def maxSubArray(nums: [int]) -> int:
    result = max(nums)

    tempmax = 0
    for n in nums:
        tempmax = tempmax + n
        result = max(result, tempmax)
        if tempmax < 0:
            tempmax = 0
    return result

assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert maxSubArray([-2,-3]) == -2
assert maxSubArray([0]) == 0