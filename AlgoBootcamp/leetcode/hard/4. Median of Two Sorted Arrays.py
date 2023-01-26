# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
from cmath import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2
        l, r = 0, len(nums1) - 1

        while True:
            indexN1 = (l + r) // 2  # we take items nums1[0:indexN1+1]
            indexN2 = half - (indexN1 + 1) - 1  # [half - (indexN1 + 1)] -> how many items to take from n2, [-1] to convert numbers to index, so we take nums2[0:indexN2+1]

            nums1Left = float(-inf)
            if indexN1 >= 0:
                nums1Left = nums1[indexN1]
            nums1Right = float(inf)
            if indexN1 + 1 < len(nums1):
                nums1Right = nums1[indexN1 + 1]

            nums2Left = float(-inf)
            if indexN2 >= 0:
                nums2Left = nums2[indexN2]
            nums2Right = float(inf)
            if indexN2 + 1 < len(nums2):
                nums2Right = nums2[indexN2 + 1]

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total % 2 == 0:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
                else:
                    return min(nums1Right, nums2Right)
            elif nums1Left > nums2Right:
                r = indexN1 - 1
            else:
                l = indexN1 + 1


sol = Solution()
assert sol.findMedianSortedArrays([1,3], [2]) == 2
assert sol.findMedianSortedArrays([1,3], [2,4]) == 2.5
