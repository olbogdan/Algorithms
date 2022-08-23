# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.

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

