# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
# Follow up: Could you use search pruning to make your solution faster with a larger board?
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen, colLen = len(board), len(board[0])

        def dfs(row, col, subWord):
            if len(subWord) == 0:
                return True
            if row < 0 or row >= rowLen or col < 0 or col >= colLen or subWord[0] != board[row][col]:
                return False

            board[row][col] = "#"
            sub = subWord[1:]
            if dfs(row - 1, col, sub) or dfs(row + 1, col, sub) or dfs(row, col - 1, sub) or dfs(row, col + 1, sub):
                return True
            else:
                board[row][col] = subWord[0]
                return False

        left = right = 0
        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == word[0]:
                    left += 1
                elif board[r][c] == word[-1]:
                    right += 1
        if left > right:
            word = word[::-1]
        for r in range(rowLen):
            for c in range(colLen):
                if dfs(r, c, word):
                    return True
        return False


sol = Solution()
assert sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB") is False
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") is True
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") is False
