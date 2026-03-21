# You are given an m x n integer matrix grid and an integer k.
#
# For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.
#
# Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.
#
# Note: If all elements in the submatrix have the same value, the answer will be 0.
#
# A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.


class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        ROW, COL = len(grid), len(grid[0])
        res = [[0] * (COL - k + 1) for _ in range(ROW - k + 1)]

        for r0 in range(ROW - k + 1):
            for c0 in range(COL - k + 1):
                arr = sorted({grid[r][c] for r in range(r0, r0 + k) for c in range(c0, c0 + k)})

                if len(arr) > 1:
                    res[r0][c0] = min(arr[i+1] - arr[i] for i in range(len(arr) - 1))

        return res


sol = Solution()
assert sol.minAbsDiff([[1,8],[3,-2]], 2) == [[2]]
assert sol.minAbsDiff([[1,-2,3],[2,3,5]], 2) == [[1,2]]
