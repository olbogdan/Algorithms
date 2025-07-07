# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
#
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
#
# Return the maximum number of events you can attend.
#
#
#
# Example 1:
#
#
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# Example 2:
#
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
#
#
# Constraints:
#
# 1 <= events.length <= 105
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 105
import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        minHeap = []
        res = 0
        i = 0
        N = len(events)
        totalDays = max(end for _, end in events)

        for day in range(1, totalDays + 1):
            # add all candidates that start date in past
            while i < N and events[i][0] <= day:
                heapq.heappush(minHeap, events[i][1])
                i += 1

            # remove expired ranges
            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)

            if minHeap:
                heapq.heappop(minHeap)
                res += 1

        return res


sol = Solution()
assert sol.maxEvents([[1, 2], [2, 3], [3, 4]]) == 3
assert sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]) == 4
