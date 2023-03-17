# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            # nS, nE, s, e -> new before curr
            # s, e, nS, nE -> new after curr
            # s, nS, nE, e -> take min start
            # nS, s, nE, e -> take max end
            if (newInterval[0] <= start <= newInterval[1]
                or start <= newInterval[0] <= end):
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
            elif newInterval[1] < start:
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            else:
                res.append(intervals[i])
        res.append(newInterval)
        return res


sol = Solution()
assert sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]) == [[1,2],[3,10],[12,16]]
assert sol.insert([[1,3],[6,9]], [2, 5]) == [[1,5],[6,9]]
