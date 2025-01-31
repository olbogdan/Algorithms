# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#
# Return the size of the largest island in grid after applying this operation.
#
# An island is a 4-directionally connected group of 1s.
#
#
#
# Example 1:
#
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:
#
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:
#
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def isOutOfGrid(r, c):
            return min(r, c) < 0 or max(r, c) == N

        curIslandId = 999

        # mark grid's cels in a land area by curIslandId
        # returns size of the lend area
        # result something like:
        # before [1, 0] after [999, 0]
        #        [1, 0]       [999, 0]
        def countSize(rootR, rootC):
            q = deque([(rootR, rootC)])
            grid[rootR][rootC] = curIslandId
            size = 0
            while q:
                size += 1
                r, c = q.popleft()
                for neiR, neiC in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
                    if not isOutOfGrid(neiR, neiC) and grid[neiR][neiC] == 1:
                        grid[neiR][neiC] = curIslandId
                        q.append((neiR, neiC))
            return size

        # map each island to island's size { curIslandId : size }
        landSize = {}
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    landSize[curIslandId] = countSize(r, c)
                    curIslandId += 1

        def connect(r, c):
            connectSize = 1
            visitLendId = []
            visitLendId.append(0)
            for neiR, neiC in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
                if isOutOfGrid(neiR, neiC) or grid[neiR][neiC] in visitLendId:
                    continue
                idOfLand = grid[neiR][neiC]
                visitLendId.append(idOfLand)
                connectSize += landSize[idOfLand]
            return connectSize

        res = 0 if len(landSize) == 0 else max(landSize.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:  # try to flip 0
                    res = max(res, connect(r, c))
        return res


sol = Solution()
assert sol.largestIsland([[1, 0], [0, 1]]) == 3
assert sol.largestIsland([[1, 1], [1, 0]]) == 4
assert sol.largestIsland([[1, 1], [1, 1]]) == 4
