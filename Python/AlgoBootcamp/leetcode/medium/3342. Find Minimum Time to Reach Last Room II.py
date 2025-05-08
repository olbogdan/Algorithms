# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
#
# Return the minimum time to reach the room (n - 1, m - 1).
#
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.
#
#
#
# Example 1:
#
# Input: moveTime = [[0,4],[4,4]]
#
# Output: 7
#
# Explanation:
#
# The minimum time required is 7 seconds.
#
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
# Example 2:
#
# Input: moveTime = [[0,0,0,0],[0,0,0,0]]
#
# Output: 6
#
# Explanation:
#
# The minimum time required is 6 seconds.
#
# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
# At time t == 3, move from room (1, 1) to room (1, 2) in one second.
# At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
# Example 3:
#
# Input: moveTime = [[0,1],[1,2]]
#
# Output: 4
#
#
#
# Constraints:
#
# 2 <= n == moveTime.length <= 750
# 2 <= m == moveTime[i].length <= 750
# 0 <= moveTime[i][j] <= 109
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rowCount, colCount = len(moveTime), len(moveTime[0])
        visited = {}
        heap = [(0, 0, 0, 1)]  # (currenttime, row, col, parity) next move 1s, 1: next move 2s

        while heap:
            currentTime, row, col, parity = heapq.heappop(heap)
            if (row, col) == (rowCount - 1, colCount - 1):
                return currentTime

            if (row, col, parity) in visited and visited[(row, col, parity)] <= currentTime:
                continue

            visited[(row, col, parity)] = currentTime

            for deltaRow, deltaCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow, newCol = row + deltaRow, col + deltaCol
                if 0 <= newRow < rowCount and 0 <= newCol < colCount:
                    moveDuration = 1 if parity == 1 else 2
                    nextTime = max(currentTime, moveTime[newRow][newCol]) + moveDuration
                    heapq.heappush(heap, (nextTime, newRow, newCol, 2 if parity == 1 else 1))

        return -1


sol = Solution()
assert sol.minTimeToReach([[0, 4], [4, 4]]) == 7
assert sol.minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]) == 6
