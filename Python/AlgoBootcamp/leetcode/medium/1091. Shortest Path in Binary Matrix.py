# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# Input: grid = [[0,1],[1,0]]
# Output: 2
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
#
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()  # row, col, len
        queue.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))

        N = len(grid)
        end = (N - 1, N - 1)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        while queue:
            r, c, length = queue.popleft()
            if min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1:
                continue
            if (r, c) == end:
                return length
            for rOffset, cOffset in directions:
                row = r + rOffset
                col = c + cOffset
                if (row, col) not in visited:
                    queue.append((row, col, length + 1))
                    visited.add((row, col))

        return -1


sol = Solution()
assert sol.shortestPathBinaryMatrix([[0,1],[1,0]]) == 2
assert sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]) == -1
