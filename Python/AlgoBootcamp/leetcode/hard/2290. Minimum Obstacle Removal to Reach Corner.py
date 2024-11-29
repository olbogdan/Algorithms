# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
#
# 0 represents an empty cell,
# 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.
#
# Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
# Output: 2
# Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
# It can be shown that we need to remove at least 2 obstacles, so we return 2.
# Note that there may be other ways to remove 2 obstacles to create a path.
# Example 2:
#
#
# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# Output: 0
# Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 2 <= m * n <= 105
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        DEST = (R-1, C-1)
        q = deque([(0, 0 , 0)])
        visit = [[False]*C for _ in range(R)]
        visit[0][0] = True
        while q:
            dist, r, c = q.popleft()
            if (r, c) == DEST:
                return dist
            dirs = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
            for nr, nc in dirs:
                if min(nr, nc) < 0 or nc == C or nr == R or visit[nr][nc]:
                    continue
                if grid[nr][nc]:
                    q.append((dist + 1, nr, nc))
                else:
                    q.appendleft((dist, nr, nc))
                visit[nr][nc] = True
        return -1


sol = Solution()
assert sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]) == 2
assert sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]) == 0
assert sol.minimumObstacles([[0,0,0],[0,0,0],[0,0,0]]) == 0
