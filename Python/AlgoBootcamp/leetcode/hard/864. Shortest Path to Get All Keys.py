# You are given an m x n grid grid where:
#
# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.
#
# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.
#
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
#
# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the locks.
# Example 2:
#
#
# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
# Example 3:
#
#
# Input: grid = ["@Aa"]
# Output: -1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either an English letter, '.', '#', or '@'.
# The number of keys in the grid is in the range [1, 6].
# Each key in the grid is unique.
# Each key in the grid has a matching lock.
from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        startX = startY = totalKeys = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    startX, startY = i, j
                elif grid[i][j].islower():
                    totalKeys += 1
        r = 0
        visited = {(startX, startY, 0)}
        q = deque([(startX, startY, 0)])
        while q:
            l = len(q)
            for _ in range(l):
                i, j, k = q.popleft()
                if k == (1 << totalKeys) - 1:
                    return r
                for x, y in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                    if rows > x >= 0 <= y < cols and grid[x][y] != "#":
                        z = k
                        if grid[x][y].islower():
                            z |= 1 << ord(grid[x][y]) - ord('a')
                        if (x, y, z) in visited or grid[x][y].isupper() and not z & (1 << ord(grid[x][y]) - ord('A')):
                            continue
                        q.append((x, y, z))
                        visited.add((x, y, z))
            r += 1
        return -1


sol = Solution()
assert sol.shortestPathAllKeys(["@..aA", "..B#.", "....b"]) == 6
