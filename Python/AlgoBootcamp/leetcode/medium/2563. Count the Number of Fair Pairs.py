# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
#
# A pair (i, j) is fair if:
#
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
#
#
# Example 1:
#
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:
#
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        # this will find if any num in nums + the current i
        # can give us sutisfactions of the lower border
        def findLowerBorder(l, numsToFind):
            r = len(nums) - 1
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= numsToFind:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res
        def findRightBorder(l, maximumNumber):
            r = len(nums) - 1
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= maximumNumber:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res


        res = 0
        for i in range(len(nums)):
            leftBorder = findLowerBorder(i+1, lower - nums[i])
            if leftBorder == -1:
                continue
            rightBorder = findRightBorder(i+1, upper - nums[i])
            if rightBorder == -1:
                continue

            res += rightBorder - leftBorder + 1
            # for j in range(leftBorder, len(nums)):
                # all numbers until the condition will be valid
                # shortcut it by finding last valid num in nums
                # number should be smaller than
                # if nums[i] + nums[j] > upper:
                #     break

                # get n where nums[i] + nums[n] >= lower
                # we want to cut off the left side that invalid to skip this check
                # we do it my this condition findLowerBorder()
                # if nums[i] + nums[j] < lower:
                #     continue
                # res += 1
        return res


s = Solution()
# assert s.countFairPairs([0,1,7,4,4,5], 3, 6) == 6
assert s.countFairPairs([1,7,9,2,5], 11, 11) == 1