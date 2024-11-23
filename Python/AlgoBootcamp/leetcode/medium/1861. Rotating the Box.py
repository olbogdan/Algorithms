# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
#
# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
#
# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
#
# Return an n x m matrix representing the box after the rotation described above.
#
#
#
# Example 1:
#
#
#
# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
# Example 2:
#
#
#
# Input: box = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
# Example 3:
#
#
#
# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
#
#
# Constraints:
#
# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'.
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box = self.createRotatedBox(box)
        return self.emulateGravitation(box)

    def emulateGravitation(self, box) -> List[List[str]]:
        STONE = '#'
        OBST = '*'
        EMPTY = '.'
        ROW = len(box)
        COL = len(box[0])
        for c in range(COL):
            bottom = ROW - 1
            for r in reversed(range(ROW)):
                if box[r][c] == OBST:
                    bottom = r - 1
                elif box[r][c] == STONE:
                    if r != bottom:
                        box[bottom][c] = STONE
                        box[r][c] = EMPTY
                    bottom -= 1
        return box

    def createRotatedBox(self, box) -> List[List[str]]:
        beforeRow = len(box)
        beforeCol = len(box[0])
        rotBox = [["."] * beforeRow for _ in range(beforeCol)]
        for bRow in range(beforeRow):
            for bCol in range(beforeCol):
                rotBox[bCol][beforeRow - bRow - 1] = box[bRow][bCol]
        return rotBox


sol = Solution()
assert sol.rotateTheBox([["#", ".", "#"]]) == [["."], ["#"], ["#"]]
assert sol.rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]) == [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]
assert sol.rotateTheBox([["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]) == [[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."], ["#", ".", "*"], ["#", ".", "."]]
