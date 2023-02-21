# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
from typing import List


def maxProduct(nums: [int]) -> int:

    allTimeMax = max(nums)
    tempMax = 1
    tempMin = 1
    for i in nums:
        temp1 = max(i, tempMax * i, tempMin * i)
        temp2 = min(i, tempMax * i, tempMin * i)
        tempMax = temp1
        tempMin = temp2
        allTimeMax = max(allTimeMax, tempMax)


    return allTimeMax


assert maxProduct([10, 0, -1, 0, 10, -1, 0, 10]) == 10
assert maxProduct([10, -1, 10, -1, 10]) == 1000
assert maxProduct([10, -1, 10, 10]) == 100
assert maxProduct([-1]) == -1


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minVal = maxVal = nums[0]
        result = max(nums)
        for i in range(1, len(nums)):
            cur = nums[i]
            newMin = min(minVal * cur, maxVal * cur, cur)
            newMax = max(minVal * cur, maxVal * cur, cur)
            minVal, maxVal = newMin, newMax
            result = max(result, newMax)
        return result


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minMax = [(1,1)]*len(nums)
        minMax[0] = (nums[0], nums[0]) # track min/max val of each step, for negative n handling
        result = max(nums)
        for i in range(1, len(nums)):
            cur = nums[i]
            cand1 = minMax[i-1][0] * cur
            cand2 = minMax[i-1][1] * cur
            minMax[i] = (min(cur, cand1, cand2), max(cur, cand1, cand2))
            result = max(result, cand1, cand2)
        return result

