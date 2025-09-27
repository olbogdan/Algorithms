# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
#
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:
#
# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
#
#
# Constraints:
#
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
from typing import List


class Solution:
    def largestTriangleArea(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i, N):
                for k in range(j, N):
                    x1 = nums[i][0]
                    x2 = nums[j][0]
                    x3 = nums[k][0]

                    y1 = nums[i][1]
                    y2 = nums[j][1]
                    y3 = nums[k][1]

                    res = max(abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))), res)
        return res


sol = Solution()
assert sol.largestTriangleArea([[1,0],[0,0],[0,1]]) == 0.50000
assert sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]) == 2.000
