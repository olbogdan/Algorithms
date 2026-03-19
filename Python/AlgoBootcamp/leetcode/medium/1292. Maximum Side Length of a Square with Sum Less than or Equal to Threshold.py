# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:
#
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105


class Solution:
    def isValid(self, pref, squareLen, limit):
        ROW, COL = len(pref), len(pref[0])

        for r in range(squareLen - 1, ROW):
            for c in range(squareLen - 1, COL):
                startR = r - squareLen + 1
                startC = c - squareLen + 1

                total = pref[r][c]
                if startR > 0:
                    total -= pref[startR - 1][c]
                if startC > 0:
                    total -= pref[r][startC - 1]
                if startR > 0 and startC > 0:
                    total += pref[startR - 1][startC - 1]

                if total <= limit:
                    return True

        return False

    def maxSideLength(self, mat, threshold):
        ROW, COL = len(mat), len(mat[0])
        pref = [row[:] for row in mat]

        for r in range(ROW):
            for c in range(1, COL):
                pref[r][c] += pref[r][c - 1]

        for c in range(COL):
            for r in range(1, ROW):
                pref[r][c] += pref[r - 1][c]

        low, high = 1, min(ROW, COL)
        res = 0

        while low <= high:
            squareLen = (low + high) // 2
            if self.isValid(pref, squareLen, threshold):
                res = squareLen
                low = squareLen + 1
            else:
                high = squareLen - 1

        return res


sol = Solution()
assert sol.maxSideLength([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4) == 2
assert sol.maxSideLength([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1) == 0
