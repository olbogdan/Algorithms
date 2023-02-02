# Given an integer array nums, return the length of the longest strictly increasing
# subsequence
# .
#
#
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lenNums = len(nums)
        candidates = [1]*lenNums
        for i in range(lenNums):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    candidates[i] = max(candidates[i], candidates[j] + 1)
        return max(candidates)


sol = Solution()
res = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
assert res == 4
res = sol.lengthOfLIS([0,1,0,3,2,3])
assert res == 4
res = sol.lengthOfLIS([7,7,7,7,7,7,7])
assert res == 1


# nlog(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            elif n <= res[0]:
                res[0] = n
            else:
                index = self.findInsertPosition(res, n)
                res[index] = n
        return len(res)

    def findInsertPosition(self, arr, n) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if n > arr[mid]:
                l = mid + 1
            else:
                r = mid
        return r


sol = Solution()
res = sol.lengthOfLIS([0,1,0,3,2,3])
assert res == 4
res = sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
assert res == 6
res = sol.lengthOfLIS([4,10,4,3,8,9])
assert res == 3