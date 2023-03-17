# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # the sum is odd
        if sum(nums) % 2:
            return False
        halfSum = sum(nums) // 2

        subsets = set()
        subsets.add(0)
        for i in range(len(nums)):
            nextSubsets = subsets.copy()
            for subN in subsets:
                subSum = subN + nums[i]
                if subSum == halfSum:
                    return True
                nextSubsets.add(subSum)
            subsets = nextSubsets
        return False


sol = Solution()
res = sol.canPartition([14,9,8,4,3,2])
assert res is True
res = sol.canPartition([1,1])
assert res is True
res = sol.canPartition([1,2])
assert res is False


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        # the sum is odd
        if sumNums % 2:
            return False
        nums.sort()
        halfSum = sumNums // 2
        if nums[-1] > halfSum:
            return False

        subsets = set()
        subsets.add(nums[0])
        for i in range(1, len(nums)):
            num = nums[i]
            if num == halfSum:
                return True
            nextSubsets = set()
            for s in subsets:
                subSum = s + num
                if subSum == halfSum:
                    return True
                elif subSum < halfSum:
                    nextSubsets.add(subSum)
                nextSubsets.add(s)
            nextSubsets.add(num)
            subsets = nextSubsets
        return False


sol = Solution2()
res = sol.canPartition([14,9,8,4,3,2])
assert res is True
