# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 9


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        usedColumns = set()
        rightDiagonal = set()
        leftDiagonal = set()

        def backtrack(row):
            if row == n:
                nonlocal result
                result += 1
                return
            for col in range(n):
                if col not in usedColumns and (row + col) not in leftDiagonal and (row - col) not in rightDiagonal:
                    usedColumns.add(col)
                    rightDiagonal.add(row - col)
                    leftDiagonal.add(row + col)
                    backtrack(row + 1)
                    usedColumns.remove(col)
                    rightDiagonal.remove(row - col)
                    leftDiagonal.remove(row + col)

        backtrack(0)
        return result


sol = Solution()
assert sol.totalNQueens(4) == 2
assert sol.totalNQueens(1) == 1
