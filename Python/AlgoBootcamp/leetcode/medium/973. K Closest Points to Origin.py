# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:
#
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#
#
# Constraints:
#
# 1 <= k <= points.length <= 104
# -104 < xi, yi < 104
from heapq import heappush, heappop
from math import inf
from typing import List


# Memory Usage: 20.3 MB, less than 81.33% of Python3
# 954 ms, faster than 83.10%
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x: (x[0]*x[0] + x[1]*x[1]))
        return points[:k]


solution = Solution()
assert solution.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert solution.kClosest([[-2,4]], 1) == [[-2,4]]


# sort()
# 795 ms, faster than 97.16%
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceList = []
        for index in range(len(points)):
            x = points[index][0]
            y = points[index][1]
            distance = x * x + y * y
            distanceList.append((distance, index))
        distanceList.sort(key=lambda x: x[0])
        result = []
        for i in range(k):
            index = distanceList[i][1]
            result.append(points[index])
        return result


solution = Solution2()
assert solution.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


# Heap with optimized memory, O(k)
class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            newMin = -(x*x + y*y)
            oldMin = minHeap[0][0] if minHeap else float(-inf)
            if newMin > oldMin or len(minHeap) < k:
                heappush(minHeap, (newMin, i))
            if len(minHeap) > k:
                heappop(minHeap)
        result = []
        while minHeap:
            dif, index = heappop(minHeap)
            result.append(points[index])
        return result


solution = Solution3()
assert solution.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert solution.kClosest([[-2,4]], 1) == [[-2,4]]