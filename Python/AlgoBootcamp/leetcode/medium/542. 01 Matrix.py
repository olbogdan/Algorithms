# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = self.findZeros(mat)
        result = [[-1] * len(mat[0]) for _ in range(len(mat))]

        level = 0
        while q:
            nextLevel = []
            for _ in range(len(q)):
                r, c = q.pop()
                if result[r][c] == -1:
                    result[r][c] = level
                for rOffset, cOffset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    rCandidate = r + rOffset
                    cCandidate = c + cOffset
                    if min(rCandidate, cCandidate) >= 0 and rCandidate < len(mat) and cCandidate < len(mat[0]) and \
                            result[rCandidate][cCandidate] == -1:
                        nextLevel.append((rCandidate, cCandidate))
            q = nextLevel
            level += 1
        return result

    def findZeros(self, mat: List[List[int]]):
        q = []
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r, c))
        return q


sol = Solution()
assert sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
