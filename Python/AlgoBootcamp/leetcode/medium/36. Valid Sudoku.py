# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = self.checkIfValidTable(board)
        if not isValid:
            return False
        rowBox = 0
        while rowBox < 9:
            colBox = 0
            while colBox < 9:
                if not self.checkIfBoxValid(board, rowBox, colBox):
                    return False
                colBox += 3
            rowBox += 3
        return True

    def checkIfValidTable(self, board) -> bool:
        for r in range(0, len(board)):
            rows = set()
            cols = set()
            for c in range(0, len(board)):
                val = board[r][c]
                if val != "." and val in rows:
                    return False
                elif val != ".":
                    rows.add(val)

                valCol = board[c][r]
                if valCol != "." and valCol in cols:
                    return False
                elif valCol != ".":
                    cols.add(valCol)
        return True

    def checkIfBoxValid(self, board, row, col) -> bool:
        boxSet = set()
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                val = board[r][c]
                if val != "." and val in boxSet:
                    return False
                elif val != ".":
                    boxSet.add(val)
        return True


solution = Solution()
isValid = solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
assert isValid is True

isValid = solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
assert isValid is False