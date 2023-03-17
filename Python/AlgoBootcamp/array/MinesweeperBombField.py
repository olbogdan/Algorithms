# create a minefield according to classincal minesweeper game rules
from typing import List

def minesweeper(bombs: List[List[int]], rows: int, columns: int) -> List[List[int]]:
    result = [[0] * columns for _ in range(rows)]

    for bomb in bombs:
        row = bomb[0]
        column = bomb[1]
        result[row][column] = -1
        for r in range(row-1, row+2):
            for c in range(column-1, column+2):
                if 0 <= r < rows and 0 <= c < columns and result[r][c] != -1:
                    result[r][c] = result[r][c]+1
    return result


def minesweeper2(bombs: List[List[int]], rows: int, columns: int) -> List[List[int]]:
    result = [[0] * columns for _ in range(rows)]

    for bomb in bombs:
        result[bomb[0]][bomb[1]] = -1

    def updateCell(row: int, column: int):
        # check 8 cells around
        # left/right/top/down edge cases at the border?
        counter = 0

        if row - 1 >= 0:
            for upColumn in range(column - 1, column + 1):
                if 0 <= upColumn < columns:
                    if result[row - 1][upColumn] == -1:
                        counter += 1

        if row + 1 < rows:
            for upColumn in range(column - 1, column + 1):
                if 0 <= upColumn < columns:
                    if result[row + 1][upColumn] == -1:
                        counter += 1

        if column - 1 >= 0:
            if result[row][column-1] == -1:
                counter += 1

        if column + 1 < columns:
            if result[row][column+1] == -1:
                counter += 1

        result[row][column] = counter

    for r in range(rows):
        for c in range(columns):
            if result[r][c] != -1:
                updateCell(r, c)

    return result


result = minesweeper([[0, 2], [0, 3]], 3, 4)
for row in result:
    print("".join(map(str, row)))

print("\n")

result = minesweeper([[0, 0], [10, 10], [15, 15], [15, 16], [19, 19]], 20, 20)
for row in result:
    print("".join(map(str, row)))
