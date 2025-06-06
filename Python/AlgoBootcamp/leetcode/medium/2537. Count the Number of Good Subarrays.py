# Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.
# Example 2:
#
# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 109


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        left = 0
        pairCount = 0
        freq = defaultdict(int)
        res = 0
        for right in range(len(nums)):
            pairCount += freq[nums[right]]
            freq[nums[right]] += 1
            while pairCount >= k:
                res += len(nums) - right
                freq[nums[left]] -= 1
                pairCount -= freq[nums[left]]
                left += 1
        return res


sol = Solution()
assert sol.countGood([1, 1, 1, 1, 1], 10) == 1
assert sol.countGood([3, 1, 4, 3, 2, 2, 4], 2) == 4
