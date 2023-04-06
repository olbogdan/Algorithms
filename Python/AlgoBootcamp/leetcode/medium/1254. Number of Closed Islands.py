# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.
#
#
#
# Example 1:
#
#
#
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
# Example 2:
#
#
#
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# Example 3:
#
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
#
#
# Constraints:
#
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        rowBorder = [0, ROWS-1]
        colBorder = [0, COLS-1]
        def isClosedIsland(r, c, curVisited):
            if (r, c) in curVisited:
                return True

            visited.add((r, c))

            if grid[r][c] == 0 and (r in rowBorder or c in colBorder):
                return False
            elif grid[r][c] == 0:
                curVisited.add((r, c))
                left = isClosedIsland(r-1, c, curVisited)
                right = isClosedIsland(r+1, c, curVisited)
                top = isClosedIsland(r, c-1, curVisited)
                bottom = isClosedIsland(r, c+1, curVisited)
                return left and right and top and bottom
            else:
                return True

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 0:
                    result += 1 if isClosedIsland(r, c, set()) else 0
        return result


sol = Solution()
res = sol.closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]])
assert res == 2
