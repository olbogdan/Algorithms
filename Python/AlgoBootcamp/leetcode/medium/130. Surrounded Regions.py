# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
from typing import List


class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        X = "X"
        O = "O"
        SAVE_O = "S"

        # mark all border O items as SAVE_O
        def bfs(r, c):
            if r < 0 or r == rows or c < 0 or c == columns or board[r][c] != O:
                return
            board[r][c] = SAVE_O
            # mark all O neighbors as SAVE_O
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c - 1)
            bfs(r, c + 1)

        for c in range(columns):
            bfs(0, c)
            bfs(rows - 1, c)

        for r in range(rows):
            bfs(r, 0)
            bfs(r, columns - 1)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == O:
                    board[r][c] = X
                elif board[r][c] == SAVE_O:
                    board[r][c] = O
        return board

sol = Solution()
res = sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
assert res == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
res = sol.solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]])
assert res == [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        def bfs(r, c, visited) -> bool:
            if r < 0 or c < 0 or r == rows or c == columns:
                return False
            if (r, c) in visited:
                return True
            if board[r][c] == "O":
                # return True if all neighbors are suraunded by x or x by themself
                visited.add((r, c))
                isolatedO = bfs(r - 1, c, visited) and bfs(r + 1, c, visited) and bfs(r, c - 1, visited) and bfs(r, c + 1, visited)
                return isolatedO
            else:
                return True
        for r in range(rows):
            for c in range(columns):
                if bfs(r, c, set()):
                    board[r][c] = "X"
        return board


sol = Solution2()
res = sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
assert res == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]