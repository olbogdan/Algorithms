# Given
# an
# integer
# array
# nums, find
# three
# numbers
# whose
# product is maximum and
# return the
# maximum
# product.
#
# Example
# 1:
#
# Input: nums = [1, 2, 3]
# Output: 6
# Example
# 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: 24
# Example
# 3:
#
# Input: nums = [-1, -2, -3]
# Output: -6

def maximumProduct(nums: [int]) -> int:
    maxOne = max(nums[0], nums[1])
    minOne = min(nums[0], nums[1])

    maxTwo = nums[0] * nums[1]
    minTwo = nums[0] * nums[1]

    maxThree = nums[0] * nums[1] * nums[2]

    for i in range(2, len(nums)):
        n = nums[i]
        tempMaxTwo = maxTwo * n
        tempMinTwo = minTwo * n
        maxThree = max(maxThree, tempMaxTwo, tempMinTwo)
        maxTwo = max(maxTwo, maxOne * n, minOne * n)
        minTwo = min(minTwo, maxOne * n, minOne * n)
        maxOne = max(maxOne, n)
        minOne = min(minOne, n)

    return maxThree

assert maximumProduct([1,2,3]) == 6
assert maximumProduct([1,2,3,4]) == 24
assert maximumProduct([1,2,3,4,5,6,7]) == 210
assert maximumProduct([7,5,6,1,2,3,4,5,6,7]) == 294
assert maximumProduct([7,-5,6,1,-2,3,-4,5,6,-7]) == 252