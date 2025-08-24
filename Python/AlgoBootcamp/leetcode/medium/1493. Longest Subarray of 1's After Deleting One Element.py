# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            if nums[i] == 0:
                prefix[i] = 0
            else:
                prefix[i] = 1 + prefix[i + 1]
        res = 0
        cur = 0
        for i in range(N):
            res = max(res, cur + prefix[i + 1])
            if nums[i] == 1:
                cur += 1
            else:
                cur = 0

        return res


sol = Solution()
assert sol.longestSubarray([1, 1, 0, 1]) == 3
assert sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
