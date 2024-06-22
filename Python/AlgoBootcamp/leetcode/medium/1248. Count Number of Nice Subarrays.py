# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#
#
# Constraints:
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        numOfOdd = 0
        l = m = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                numOfOdd += 1
            # if too much odd, shift l
            while numOfOdd > k:
                if nums[l] % 2:
                    numOfOdd -= 1
                l += 1
                m = l

            if numOfOdd == k:
                # move m to extend the max valid range
                while nums[m] % 2 == 0:
                    m += 1
                res += m + 1 - l
        return res


s = Solution()
assert s.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert s.numberOfSubarrays([2, 4, 6], 1) == 0
