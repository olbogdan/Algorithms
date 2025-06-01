# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
#
# You start on square 1 of the board. In each move, starting from square curr, do the following:
#
# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.
#
# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.
#
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.
#
#
#
# Example 1:
#
#
# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.
# Example 2:
#
# Input: board = [[-1,-1],[-1,3]]
# Output: 1
#
#
# Constraints:
#
# n == board.length == board[i].length
# 2 <= n <= 20
# board[i][j] is either -1 or in the range [1, n2].
# The squares labeled 1 and n2 are not the starting points of any snake or ladder.
from collections import deque
from typing import List


class Solution:
    def getCoordinates(self, dest, n):
        row = (dest - 1) // n
        col = (dest - 1) % n
        if row % 2 == 1:  # convert odd rows go right to left
            col = n - 1 - col
        row = n - 1 - row  # convert bottom up
        return row, col

    def getNextPosition(self, square, board, n):
        row, col = self.getCoordinates(square, n)
        if board[row][col] != -1:
            return board[row][col]
        return square

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        TARGET = N * N
        queue = deque([1])
        visited = {1}
        level = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == TARGET:
                    return level
                for dice in range(1, 7):
                    destination = current + dice
                    if destination > TARGET:
                        break

                    destination = self.getNextPosition(destination, board, N)

                    if destination not in visited:
                        visited.add(destination)
                        queue.append(destination)
            level += 1
        return -1


sol = Solution()
assert sol.snakesAndLadders([[-1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1],
                       [-1, 35, -1, -1, 13, -1],
                       [-1, -1, -1, -1, -1, -1],
                       [-1, 15, -1, -1, -1, -1]]) == 4

assert sol.snakesAndLadders([[-1,-1],[-1,3]]) == 1