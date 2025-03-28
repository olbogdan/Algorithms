# You are given an m x n integer matrix grid and an array queries of size k.
#
# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
#
# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
#
# Return the resulting array answer.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.
# Example 2:
#
#
# Input: grid = [[5,2,1],[1,1,2]], queries = [3]
# Output: [0]
# Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= grid[i][j], queries[i] <= 106
from heapq import heappop, heappush
from typing import List


class Solution:
    def prepareQueries(self, queries):
        res = []
        for idx, val in enumerate(queries):
            res.append((val, idx))
        res.sort()
        return res

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query = self.prepareQueries(queries) # [(val, idx)]
        pq = [(grid[0][0], 0, 0)]
        visit = set([(0, 0)])
        res = [0] * len(queries)
        runSum = 0
        for qVal, qIdx in query:
            while pq and pq[0][0] < qVal:
                runSum += 1
                _, row, col = heappop(pq)
                dir = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
                for neiR, neiC in dir:
                    if (min(neiR, neiC) >= 0
                        and neiR < len(grid)
                        and neiC < len(grid[0])
                        and (neiR, neiC) not in visit
                    ):
                        visit.add((neiR, neiC))
                        heappush(pq, (grid[neiR][neiC], neiR, neiC))
            res[qIdx] = runSum
        return res


sol = Solution()
assert sol.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]) == [5,8,1]
assert sol.maxPoints([[5,2,1],[1,1,2]], [3]) == [0]
