#Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Example 1:
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        resultIntervals = []
        resultIntervals.append(intervals[0])
        for i in range(1, len(intervals)):
            prevEnd = resultIntervals[-1][1]
            curStart = intervals[i][0]
            if curStart < prevEnd:
                resultIntervals[-1][1] = min(intervals[i][1], resultIntervals[-1][1])
            else:
                resultIntervals.append(intervals[i])
        return len(intervals) - len(resultIntervals)


sol = Solution()
assert sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert sol.eraseOverlapIntervals([[1,2],[2,3]]) == 0
assert sol.eraseOverlapIntervals([[1,2]]) == 0


def eraseOverlapIntervals(intervals: [[int]]) -> int:
    intervals.sort(key=lambda x: x[1])

    maxCountNotOverlapping = 1
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        localBegin = intervals[i][0]
        localEnd = intervals[i][1]
        if localBegin < end:
            continue

        maxCountNotOverlapping += 1
        end = localEnd

    return len(intervals) - maxCountNotOverlapping

assert eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert eraseOverlapIntervals([[1,2],[2,3]]) == 0
assert eraseOverlapIntervals([[1,2]]) == 0