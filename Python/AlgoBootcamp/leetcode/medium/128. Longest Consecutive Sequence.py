# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        result = 0
        for n in numsset:
            # cur n is beginning of a sequence
            if (n - 1) not in numsset:
                r = 1
                while (n + r) in numsset:
                    r += 1
                result = max(result, r)
        return result


sol = Solution()
assert sol.longestConsecutive([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]) == 10
assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
