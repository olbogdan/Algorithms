# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
#
#
#
# Example 1:
#
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:
#
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
#
#
# Constraints:
#
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104
# 1 <= k <= arr.length
# 0 <= threshold <= 104
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        slow = 0
        result = 0
        curSum = sum(arr[:k-1])
        while slow+k-1 < len(arr):
            curSum += arr[slow+k-1]
            if curSum/k >= threshold:
                result += 1
            curSum -= arr[slow]
            slow += 1
        return result


sol = Solution()
result = sol.numOfSubarrays([2,5,8], 1, 3)
assert result == 2
result = sol.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)
assert result == 3
