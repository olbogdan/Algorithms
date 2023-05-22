# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
#
# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
#
# You may change 0's to 1's to connect the two islands to form one island.
#
# Return the smallest number of 0's you must flip to connect the two islands.
#
#
#
# Example 1:
#
# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:
#
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:
#
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
from collections import deque
from typing import List, Tuple


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        firstLand = self.findLand(grid)
        watterFront, visitedLand = self.findWatterFront(grid, firstLand)
        return self.findClosestLand(grid, watterFront, visitedLand)

    def findClosestLand(self, grid: List[List[int]], watterFront: set, visited: set) -> int:
        q = deque(watterFront)
        distance = 0
        while q:
            N = len(q)
            for _ in range(N):
                r, c = q.popleft()
                if (r, c) in visited or min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                visited.add((r, c))
                if grid[r][c] == 1:
                    return distance
                q.append([r - 1, c])
                q.append([r + 1, c])
                q.append([r, c - 1])
                q.append([r, c + 1])
            distance += 1
        return 9999999999

    def findWatterFront(self, grid: List[List[int]], land: List[int]) -> Tuple[set, set]:
        watter = set()
        visitedLand = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if (r, c) in visitedLand or (r, c) in watter:
                return

            if grid[r][c] == 0:
                watter.add((r, c))
            else:
                visitedLand.add((r, c))
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)

        dfs(land[0], land[1])
        return (watter, visitedLand)

    def findLand(self, grid: List[List[int]]) -> List[int]:
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 1:
                    return [r, c]
        raise Exception("Grid has no land")


sol = Solution()
assert sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]) == 1
assert sol.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]) == 2
