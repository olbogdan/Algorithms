# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
from cmath import inf
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # in worst case the missing integer at the end of len([1, 2, 3, 4, 5])+1 -> N+1
        # if we would have extra space, add all positive nums to a hash set and iterate N times
        # else use input as a cache

        # clean up input from invalid nums, replace minuses in [-1, -2, 0, 3, 4] by 0
        N = len(nums)
        for i in range(N):
            if nums[i] < 0:
                nums[i] = 0

        # use minus value to indicate that item at position i exist
        # associate mapping [idx0 = val 1, idx1 = val 2]
        for i in range(N):
            value = abs(nums[i])
            # value in valid range
            if 0 < value <= N:
                idxToInvert = value - 1
                if nums[idxToInvert] > 0:
                    nums[idxToInvert] *= -1
                elif nums[idxToInvert] == 0:
                    nums[idxToInvert] = float(-inf)

        # we get a cache as [-1, -3, -inf, -2] means all values 1 to N exist - the answer N+1
        # we get a cache as [-1, 4, -inf, -2] means value 2 does not exist, return it
        # [-1, -4, 0, -2] 0 means at position is not found, return idx of val 0 + 1
        for i in range(N):
            if nums[i] >= 0:
                return i + 1
        return N + 1


sol = Solution()
assert sol.firstMissingPositive([3,4,-1,1]) == 2
assert sol.firstMissingPositive([7,8,9,11,12]) == 1


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        end = self.movePositiveToTheBeginigng(nums)

        # sub array contains only values 1 .. positive
        # ignore values that greater then end
        # reuse cells by setting them negative to indicate the value was found
        for i in range(end):
            value = abs(nums[i])
            if value - 1 < end:
                if nums[i - 1] > 0:  # nums[i - 1] used as cache
                    nums[i - 1] = -nums[i - 1]
        for i in range(end):
            if nums[i] > 0:
                return i + 1
        return end + 1

    # returns pivot, shows begining of 0 or negative partition
    def movePositiveToTheBeginigng(self, nums) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] > 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return slow


sol = Solution2()
assert sol.firstMissingPositive([3,4,-1,1]) == 2
# assert sol.firstMissingPositive([7,8,9,11,12]) == 1
