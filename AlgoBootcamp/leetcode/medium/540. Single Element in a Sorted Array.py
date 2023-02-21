# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # always have odd number of items
        # best case 1: [1,1,2(mid),3,3] -> i-1 != mid != i+1
        # [0,1,1(m),3,3] -> [0,1,1]
        # [0,0,1(m),1,3] -> [1,1,3]
        # [0,0,A,2(m),2,3,3]
        # case 2: [0,0,2,2,3(mid),3,A,4,4] -> i-1 == mid -> search in side that has odd number
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if mid-1 >= 0 and nums[mid-1] == nums[mid]:
                # pair with left element found
                if (mid-1 - l) % 2 == 1:
                    r = mid-2
                else:
                    l = mid+1
            elif mid+1 < len(nums) and nums[mid+1] == nums[mid]:
                # pair with right element found
                if (r - mid+1) % 2 == 1:
                    l = mid+2
                else:
                    r = mid-1
            else:
                # mid has no pair, single element found
                return nums[mid]


sol = Solution()
res = sol.singleNonDuplicate([3,3,7,7,10,11,11])
assert res == 10
res = sol.singleNonDuplicate([1,1,2,2,3])
assert res == 3
