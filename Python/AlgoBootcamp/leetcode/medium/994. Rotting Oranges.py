# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        spoiled = deque()
        countOfFresh = 0
        rows = len(grid)
        columns = len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    spoiled.append((r, c))
                if grid[r][c] == 1:
                    countOfFresh += 1

        adjacentDirections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # while we have somthing in spoiled queue take it
        minutes = 0
        while spoiled and countOfFresh > 0:
            partOfQueue = len(spoiled)
            for i in range(partOfQueue):
                r, c = spoiled.popleft()
                for rOffset, cOffset in adjacentDirections:
                    row = r + rOffset
                    col = c + cOffset
                    if row in range(rows) and col in range(columns) and grid[row][col] == 1:
                        grid[row][col] = 2
                        countOfFresh -= 1
                        spoiled.append((row, col))
            minutes += 1

        if countOfFresh > 0:
            return -1
        return minutes


sol = Solution()
res = sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
assert res == 4
res = sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
assert res == -1
res = sol.orangesRotting([[0,2]])
assert res == 0


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        spoiled = []
        countOfFresh = 0
        rows = len(grid)
        columns = len(grid[0])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    spoiled.append((r, c))
                if grid[r][c] == 1:
                    countOfFresh += 1

        mapOfSpoiling = {}

        def dfs(r, c, minute):
            if r < 0 or c < 0 or r == rows or c == columns or grid[r][c] != 1:
                return
            if (r, c) in mapOfSpoiling and mapOfSpoiling[(r, c)] <= minute:
                return
            mapOfSpoiling[(r, c)] = minute
            dfs(r + 1, c, minute + 1)
            dfs(r - 1, c, minute + 1)
            dfs(r, c + 1, minute + 1)
            dfs(r, c - 1, minute + 1)

        for r, c in spoiled:
            dfs(r + 1, c, 1)
            dfs(r - 1, c, 1)
            dfs(r, c + 1, 1)
            dfs(r, c - 1, 1)

        if countOfFresh == 0:
            return 0
        if len(mapOfSpoiling) < countOfFresh:
            return -1
        return max(mapOfSpoiling.values())


sol = Solution2()
res = sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
assert res == 4
res = sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
assert res == -1
res = sol.orangesRotting([[0,2]])
assert res == 0
