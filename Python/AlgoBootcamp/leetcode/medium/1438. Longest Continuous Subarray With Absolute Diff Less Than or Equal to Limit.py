# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
#
#
#
# Example 1:
#
# Input: nums = [8,2,4,7], limit = 4
# Output: 2
# Explanation: All subarrays are:
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4.
# Therefore, the size of the longest subarray is 2.
# Example 2:
#
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:
#
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # [1, 4, 2, 5, 7] l = 3
        counter = defaultdict(int)
        dqMin = []
        dqMax = []

        def clearFromDeadNumbers():
            while counter[dqMin[0]] == 0:
                heappop(dqMin)
            while counter[dqMax[0] * -1] == 0:
                heappop(dqMax)

        result = 0
        l = 0
        for r in range(len(nums)):
            heappush(dqMin, nums[r])
            heappush(dqMax, (nums[r] * -1))
            counter[nums[r]] += 1

            while (dqMax[0] * -1) - dqMin[0] > limit:
                counter[nums[l]] -= 1
                l += 1
                clearFromDeadNumbers()
            result = max(result, r - l + 1)
        return result


s = Solution()
assert s.longestSubarray([8, 2, 4, 7], 4) == 2
assert s.longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4
