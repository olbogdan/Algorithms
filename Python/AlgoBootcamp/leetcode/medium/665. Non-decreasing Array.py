# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
#
#
#
# Example 1:
#
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
#
# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105
from cmath import inf
from typing import List


class Solution:
  def checkPossibility(self, nums: List[int]) -> bool:
    if len(nums) == 1:
      return True
    modified = False
    for i in range(len(nums) - 1):
      if nums[i] <= nums[i + 1]:
        continue
      if modified:
        return False
      modified = True
      # try to minimize prev before maximizing next
      if i == 0 or nums[i - 1] <= nums[i + 1]:
        nums[i] = nums[i + 1]
      else:
        nums[i + 1] = nums[i]
    return True


sol = Solution()
res = sol.checkPossibility([2, 3, 3, 2, 2])
assert res is False
res = sol.checkPossibility([2, 3, 2, 2])
assert res is True


class Solution2:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        modified = False
        prevLeftMax = float(-inf)
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                prevLeftMax = nums[i]
            else:
                if modified:
                    return False
                modified = True
                # try to minimize prev before maximizing next
                if prevLeftMax <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        return True


sol = Solution2()
res = sol.checkPossibility([2, 3, 3, 2, 2])
assert res is False
res = sol.checkPossibility([2, 3, 2, 2])
assert res is True
