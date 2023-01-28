# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
#
# Input: n = 1
# Output: [["Q"]]
#
#
# Constraints:
#
# 1 <= n <= 9
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []

        for i in range(n):
            subArr = []
            for j in range(n):
                subArr.append(".")
            board.append(subArr)
        # board = [ ["."*n for i in range(n)]]

        columns = set()
        rightDiagonal = set()
        leftDiagonal = set()

        def dfs(row):
            if row == n:
                # dump all subresults to result
                copy = []
                for subArr in board:
                    copy.append("".join(subArr))
                result.append(copy)
                # result.append(["".join(subRow) for subRow in board)])
                return
            for col in range(n):
                if col not in columns and (row - col) not in rightDiagonal and (row + col) not in leftDiagonal:
                    board[row][col] = "Q"
                    # disable col, right and left diagonales
                    columns.add(col)
                    rightDiagonal.add(row - col)
                    leftDiagonal.add(row + col)
                    dfs(row + 1)
                    # enable col, right and left diagonales
                    board[row][col] = "."
                    columns.remove(col)
                    rightDiagonal.remove(row - col)
                    leftDiagonal.remove(row + col)

        dfs(0)
        return result


sol = Solution()
assert sol.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]