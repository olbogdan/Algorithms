# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
#
#
# Example 1:
#
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:
#
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
#
#
# Constraints:
#
# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for encoded in timePoints:
            minutes = int(encoded[3:])
            hours = int(encoded[:2])
            times.append(hours*60+minutes)
        times.sort()
        minDif = 24*60 + times[0] - times[-1]
        for i in range(1, len(times)):
            minDif = min(minDif, times[i] - times[i-1])
        return minDif


sol = Solution()
assert sol.findMinDifference(["23:59","00:00"]) == 1
assert sol.findMinDifference(["00:00","23:59","00:00"]) == 0
