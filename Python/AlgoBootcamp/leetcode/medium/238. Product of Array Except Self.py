# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# O(1) memory, result is not counted
def productExceptSelf(nums: [int]) -> [int]:
    result = [1] * len(nums)
    product = 1
    i = 0
    while i < len(nums):
        result[i] = product
        product *= nums[i]
        i += 1

    product = 1
    i = len(nums) - 1
    while i >= 0:
        result[i] *= product
        product *= nums[i]
        i -= 1
    return result

assert productExceptSelf([1, 2, 3, 4]) == [24,12,8,6]


# O(n) memory
def productExceptSelf(nums: [int]) -> [int]:
    prefix = [1] * len(nums)
    prev = 1
    for i in range(len(nums)):
        prefix[i] = nums[i] * prev
        prev = prefix[i]

    postfix = [1] * len(nums)
    prev = 1
    for i in range(len(nums) - 1, -1, -1):
        postfix[i] = nums[i] * prev
        prev = postfix[i]

    result = [1] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            result[i] = postfix[i + 1]
            continue
        if i == len(nums) - 1:
            result[i] = prefix[i - 1]
            continue
        result[i] = prefix[i - 1] * postfix[i + 1]
    return result
