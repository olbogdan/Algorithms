# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums: [int]) -> int:
    result = 0
    for i in nums:
        result = result ^ i
    return result

assert singleNumber([2,2,1]) == 1
assert singleNumber([2,2,4,5,6,6,5]) == 4