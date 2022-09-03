from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashNums = {}
    for i in range(0, len(nums)):
        num = nums[i]
        searchedNum = target - num
        if searchedNum in hashNums:
            index = hashNums[searchedNum]
            return [index, i]
        hashNums[nums[i]] = i

assert twoSum([2,7,11,15], 9) == [0,1]
assert twoSum([3,2,4], 6) == [1,2]
assert twoSum([3, 3], 6) == [0,1]
assert twoSum([-1,-2,-3,-4,-5], -8) == [2,4]