
from typing import List


class Square:
    def __init__(self, value='#'):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        print(f"Setting the value ...")
        if value == None:
            raise Exception("value must be passed")
        if value == '#':
            value = 0
        if value < 0 or value > 9:
            raise ValueError(
                'Invalid sudoku entry. Use a number between 1 and 9 or a # to represent an empty space')
        self._value = value

    def __repr__(self):
        return f"{self._value}" if self._value else "#"

    def __eq__(self, other):
        if hasattr(other, 'value'):
            return self.value == other.value
        return self.value == other

    def __ne__(self, other):
        if hasattr(other, 'value'):
            return self.value != other.value
        return self.value != other


class Solver:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_unassigned() -> (int, int):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row, col
            return -1, -1

        def is_valid(row: int, col: int, character: str) -> bool:
            is_row_safe = all(board[row][_] != character for _ in range(9))
            is_col_safe = all(board[_][col] != character for _ in range(9))

            row_start = (row//3) * 3
            col_start = (col//3) * 3

            for row in range(row_start, row_start + 3):
                for col in range(col_start, col_start + 3):
                    if board[row][col] == character:
                        return False
            return is_row_safe and is_col_safe

        def solve() -> bool:
            row, col = find_unassigned()
            if (row, col) == (-1, -1):
                return True
            for num in map(str, range(1, 10)):
                if is_valid(row, col, num):
                    board[row][col] = num
                    if solve() == True:
                        return True
                    # backtrack
                    board[row][col] = '.'
                # print(f"{i=}:{num=}")

        solve()


def print_board(board: List[List[str]]) -> None:
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(board[0])):
            # handle starting and minisquare boundary
            if j % 3 == 0 or j == 0:
                print("|", end="")
            if j == 8:  # handle last row boundary case
                print(board[i][j], end="| \n")
            else:
                print(str(board[i][j]), end=" ")


def solve_sudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def find_unassigned() -> (int, int):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return row, col
        return -1, -1

    def is_valid(row: int, col: int, character: str) -> bool:
        is_row_safe = all(board[row][_] != character for _ in range(9))
        is_col_safe = all(board[_][col] != character for _ in range(9))

        row_start = (row//3) * 3
        col_start = (col//3) * 3

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if board[row][col] == character:
                    return False
        return is_row_safe and is_col_safe

    def solve() -> None:
        row, col = find_unassigned()
        if (row, col) == (-1, -1):
            return True
        for num in map(str, range(1, 10)):
            if is_valid(row, col, num):
                board[row][col] = num
                if solve():
                    return True
                # backtrack
                board[row][col] = '.'
            # print(f"{i=}:{num=}")

    solve()


def main():
    sq1 = Square()
    sq1.value = 3
    print(sq1)
    sq2 = Square(3)
    print(sq1 == sq2)
    # example_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # # print_board(example_board)
    # print_board(example_board)
    # solve_sudoku(board=example_board)
    # print()
    # print()
    # print_board(example_board)


if __name__ == "__main__":
    main()
