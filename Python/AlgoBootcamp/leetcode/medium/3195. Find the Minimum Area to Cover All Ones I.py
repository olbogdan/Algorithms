# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.
#
# Return the minimum possible area of the rectangle.
#
#
#
# Example 1:
#
# Input: grid = [[0,1,0],[1,0,1]]
#
# Output: 6
#
# Explanation:
#
#
#
# The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.
#
# Example 2:
#
# Input: grid = [[1,0],[0,0]]
#
# Output: 1
#
# Explanation:
#
#
#
# The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.
#
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 0 or 1.
# The input is generated such that there is at least one 1 in grid.
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        l = r = -1
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    if l == -1:
                        l = row
                    r = row
                    break
        l1 = r1 = -1
        for col in range(COL):
            for row in range(ROW):
                if grid[row][col] == 1:
                    if l1 == -1:
                        l1 = col
                    r1 = col
                    break
        return (r - l + 1) * (r1 - l1 + 1)


sol = Solution()
assert sol.minimumArea([[0, 1, 0], [1, 0, 1]]) == 6
assert sol.minimumArea([[1, 0], [0, 0]]) == 1
