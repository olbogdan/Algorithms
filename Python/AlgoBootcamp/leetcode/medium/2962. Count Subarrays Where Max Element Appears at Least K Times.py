# You are given an integer array nums and a positive integer k.
#
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
#
# A subarray is a contiguous sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
# Example 2:
#
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        totalSubarrays = (N * (N + 1)) // 2
        # lets count how many subarrays where k appears less then k and substract it from total
        subarrays = 0
        maxNumber = max(nums)
        repeat = 0
        l = 0
        for r in range(N):
            if nums[r] == maxNumber:
                repeat += 1
            while repeat >= k:
                if nums[l] == maxNumber:
                    repeat -= 1
                l += 1
            subarrays += r - l + 1

        return totalSubarrays - subarrays


sol = Solution()
assert sol.countSubarrays([1, 3, 2, 3, 3], 2) == 6
assert sol.countSubarrays([1, 4, 2, 1], 3) == 0
