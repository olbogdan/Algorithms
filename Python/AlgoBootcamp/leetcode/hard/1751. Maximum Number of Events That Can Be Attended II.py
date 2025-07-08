# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
#
# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
#
# Return the maximum sum of values that you can receive by attending events.
#
#
#
# Example 1:
#
#
#
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
# Example 2:
#
#
#
# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
# Example 3:
#
#
#
# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
#
#
# Constraints:
#
# 1 <= k <= events.length
# 1 <= k * events.length <= 106
# 1 <= startDayi <= endDayi <= 109
# 1 <= valuei <= 106
import bisect
from functools import cache
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        if k == 1:  # optimization for TLE
            return max([event[2] for event in events])

        events.sort()
        eventStarts = [event[0] for event in events]  # enables binary search

        @cache
        def dp(i, inrK):
            if inrK == 0 or i >= len(events):
                return 0

            maxScore = events[i][2]

            # get minimum index where start day is greater than current end day
            nextIndexMinimum = bisect.bisect_left(eventStarts, events[i][1] + 1)
            maxScore = max(maxScore, events[i][2] + dp(nextIndexMinimum, inrK - 1))

            # check if we can get a better score if we skip this index
            maxScore = max(maxScore, dp(i + 1, inrK))

            return maxScore

        return dp(0, k)


sol = Solution()
assert sol.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2) == 7
assert sol.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2) == 10
