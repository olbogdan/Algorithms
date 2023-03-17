from collections import deque
from typing import List
# You are given an m x n char matrix field
# 0 - not opened
# digit ('1' to '8') represents how many mines are adjacent to this revealed square
# -1 bomb
# You are also given an integer array click where click = [clickr, clickc]
# represents the next click position among all the unrevealed squares
# on click open all not opened, connected to a click area squares by marking them as -2
# X revealed mine
from AlgoBootcamp.array.MinesweeperBombField import minesweeper

def clickMineSweeperBFS(field: List[List[int]], click: List[int]) -> List[List[int]]:
    clickRow = click[0]
    clickColomn = click[1]

    rows = len(field)
    columns = len(field[0])

    queue = deque()
    queue.append([clickRow, clickColomn])

    while queue:
        cell = queue.pop()
        if field[cell[0]][cell[1]] == 0:
            field[cell[0]][cell[1]] = -2

            for r in range(cell[0]-1, cell[0]+2):
                for c in range(cell[1]-1, cell[1]+2):
                    if 0 <= r < rows and 0 <= c < columns and field[r][c] == 0:
                        queue.append((r, c))

    return field

def clickMineSweeperRecursive(field: List[List[int]], click: List[int]) -> List[List[int]]:
    clickRow = click[0]
    clickColomn = click[1]
    rows = len(field)
    columns = len(field[0])

    if clickRow < 0 or clickRow == rows or clickColomn < 0 or clickColomn == columns:
        return field

    if field[clickRow][clickColomn] == 0:
        field[clickRow][clickColomn] = -2
        for r in range(clickRow-1, clickRow+2):
            for c in range(clickColomn-1, clickColomn+2):
                clickMineSweeperRecursive(field, [r, c])
    return field

field = minesweeper([[0, 3], [1, 3], [4, 0]], 10, 10)
result = clickMineSweeperBFS(field, [6, 1])
for row in result:
    print("     ".join(map(str, row)))

print("\n")