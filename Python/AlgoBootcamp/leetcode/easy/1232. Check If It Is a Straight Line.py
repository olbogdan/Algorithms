# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#
#
#
#
#
# Example 1:
#
#
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:
#
#
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
#
# Constraints:
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
from cmath import inf
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slope = (y1 - y2) / (x1 - x2)
        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        slope = float(inf)
        if x1 != x2:
            slope = (y1 - y2) / (x1 - x2)

        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i][0], coordinates[i][1]
            if x1 == x2 and x1 == x3:
                continue
            elif (x1 == x2 and x1 != x3) or (x1 != x2 and x1 == x3):
                return False

            slope3 = (y1 - y3) / (x1 - x3)
            if slope != slope3:
                return False
        return True


sol = Solution()
assert sol.checkStraightLine([[1,-8],[2,-3],[1,2]]) is False
assert sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) is True
