# Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
# A good array is an array where the number of different integers in that array is exactly k.
#
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:
#
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length
from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        subarrays1 = self._subarraysWithKDistinct(nums, k - 1)
        subarrays2 = self._subarraysWithKDistinct(nums, k)
        return subarrays2 - subarrays1

    def _subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        l = 0
        result = 0
        for r in range(len(nums)):
            memo[nums[r]] += 1
            while len(memo) > k:
                memo[nums[l]] -= 1
                if memo[nums[l]] == 0:
                    memo.pop(nums[l])
                l += 1
            result += (r - l + 1)
        return result


sol = Solution()
assert sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7
assert sol.subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3
