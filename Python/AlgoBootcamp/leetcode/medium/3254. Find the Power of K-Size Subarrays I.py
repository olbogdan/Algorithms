# You are given an array of integers nums of length n and a positive integer k.
#
# The power of an array is defined as:
#
# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all
# subarrays
#  of nums of size k.
#
# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,3,2,5], k = 3
#
# Output: [3,4,-1,-1,-1]
#
# Explanation:
#
# There are 5 subarrays of nums of size 3:
#
# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.
# Example 2:
#
# Input: nums = [2,2,2,2,2], k = 4
#
# Output: [-1,-1]
#
# Example 3:
#
# Input: nums = [3,2,3,2,3,2], k = 2
#
# Output: [-1,3,-1,3,-1]
#
#
#
# Constraints:
#
# 1 <= n == nums.length <= 500
# 1 <= nums[i] <= 105
# 1 <= k <= n
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        # len 5 [0, 1, 2, 3, 4]
        breakingIdx = -1
        for i in range(len(nums) - k + 1):
            # optimize 1: to not repeat broken sequence
            if i < breakingIdx:
                res.append(-1)
                continue

            # optimize 2: dont repeat success sequence
            if res and nums[i + k - 1] - res[-1] == 1:
                res.append(nums[i + k - 1])
                continue

            prev = nums[i]
            curMax = prev
            for j in range(i + 1, i + k):
                if nums[j] - prev != 1:  # braking order
                    breakingIdx = j
                    curMax = -1
                    break
                prev = nums[j]
                curMax = max(curMax, nums[j])
            res.append(curMax)
        return res


s = Solution()
assert s.resultsArray([1, 2, 3, 4, 3, 2, 5], 3) == [3, 4, -1, -1, -1]
assert s.resultsArray([2, 2, 2, 2, 2], 4) == [-1, -1]
