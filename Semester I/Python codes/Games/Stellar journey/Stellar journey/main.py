import random
from texttable import Texttable

class Board():
    def __init__(self, rows, cols, endeavour, enemy_ship, stars):
        self._rows = rows
        self._cols = cols
        self._endeavour = endeavour
        self._enemy_ship = enemy_ship
        self._stars = stars
        self._data = [[" " for i in range(self._cols)] for j in range(self._rows)]
        self._visibility = [[False for j in range(self._cols)] for i in range(self._rows)]
        #self._data = []
        self._lay_stars()
        self._place_endeavour()


    def _hide(self, row, col):
        if self._data[row][col] == "B":
            self._visibility[row][col] = True

    def _row_repr(self, row: list) -> list:
        result = []
        for symbol in row:
            if symbol is None:
                result.append(' ')
            else:
                result.append(symbol)
        return result

    def _reveal_enemy_ship(self, row, col):
        if self._data[row][col] == "B":
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not self._on_board(row + i, col + j):
                        continue
                    if self._data[row + i][col + j] == "E":
                        self._visibility[row][col] = False
                        return True

    def __str__(self):

        board = Texttable()
        #board header
        board.header(['0'] + list(range(1, self._cols + 1)))

        #board.add_row(['A'] + self._row_repr(self._data[0]))
        #for i in range(self._cols - 1):
            #board.add_row([chr(ord('B') + i)] + self._row_repr(self._data[i + 1]))
        for row in range(self._rows):
            visible_element = self._data[row][:]
            for i in range(self._cols):
                self._hide(row, i)
                if self._reveal_enemy_ship(row, i) is True:
                    visible_element[i] = "B"
                if self._visibility[row][i] is True:
                    visible_element[i] = " "
                    #continue
            board.add_row([chr(ord('A') + row)] + visible_element)
        return board.draw()

    def _cheat_board(self):
        board = Texttable()
        # board header
        board.header(['0'] + list(range(1, self._cols + 1)))

        board.add_row(['A'] + self._row_repr(self._data[0]))
        for i in range(self._cols - 1):
            board.add_row([chr(ord('B') + i)] + self._row_repr(self._data[i + 1]))
        return board.draw()


    def _on_board(self, row, col: int) -> bool:
        return 0 <= row < self._rows and 0 <= col < self._cols

    def _lay_stars(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        self._data[x][y] = "*"
        for i in range(self._stars - 1):
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            while self._check_neighbour(x, y) is False:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
            self._data[x][y] = "*"

    def _place_endeavour(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        while self._check_stars(x, y) is False:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
        self._data[x][y] = "E"

    def _place_enemy_ship(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if self._data[row][col] == "B":
                    self._data[row][col] = " "

        x = random.randint(0, 7)
        y = random.randint(0, 7)
        for i in range(self._enemy_ship):
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            while self._check_stars(x, y) is False and self._check_endeavour(x, y):
                x = random.randint(0, 7)
                y = random.randint(0, 7)
            self._data[x][y] = "B"

    def _check_neighbour(self, check_row, check_col):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not self._on_board(check_row + i, check_col + j):
                    continue
                if self._data[check_row + i][check_col + j] != " ":
                    return False
        return True

    def _check_stars(self, check_row, check_col):
        if self._data[check_row][check_col] == "*":
            return False
        return True

    def _check_endeavour(self, check_row, check_col):
        if self._data[check_row][check_col] == "E":
            return False
        return True

    def _get_position_of_endeavour(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if self._data[row][col] == "E":
                    return row, col

    def _simulate_move(self, row, col):
        if self._check_hor(row, col) or self._check_vert(row, col) or self._check_main_diag(row, col) or self._check_sec_diag(row, col):
            return True
        return False

    def _move(self, row, col):
        if self._simulate_move(row, col):
            end_row, end_col = self._get_position_of_endeavour()
            self._data[row][col] = "E"
            self._data[end_row][end_col] = " "
            return True
        return False

    def _is_lose(self, row, col):
        if self._simulate_move(row, col) and self._data[row][col] == "B":
            return True
        return False

    def _is_win(self):
        if self._enemy_ship == 0:
            return True
        return False

    def _check_vert(self, row, col):
        end_row, end_col = self._get_position_of_endeavour()
        if col != end_col:
            return False
        if end_row < row:
            for x in range(end_row, row):
                if self._data[x][col] == "*":
                    return False
        if end_row > row:
            for x in range(row, end_row):
                if self._data[x][col] == "*":
                    return False
        return True

    def _check_hor(self, row, col):
        end_row, end_col = self._get_position_of_endeavour()
        if row != end_row:
            return False
        if end_col < col:
            for x in range(end_col, col):
                if self._data[row][x] == "*":
                    return False
        if end_col > col:
            for x in range(col, end_col):
                if self._data[row][x] == "*":
                    return False
        return True

    def _check_main_diag(self, row, col):
        end_row, end_col = self._get_position_of_endeavour()
        if abs(row - end_row) != abs(col - end_col):
            return False
        for x in range(abs(row - end_row)):
            if not self._on_board(end_row + x, end_col + x) or not self._on_board(end_row - x, end_col - x):
                continue
            if self._data[end_row + x][end_col + x] == "*" or self._data[end_row - x][end_col - x] == "*":
                return False
        return True

    def _check_sec_diag(self, row, col):
        end_row, end_col = self._get_position_of_endeavour()
        if abs(row - end_row) != abs(col - end_col):
            return False

        for x in range(abs(row - end_row)):
            if not self._on_board(end_row + x, end_col - x) or not self._on_board(end_row - x, end_col + x):
                continue
            if self._data[end_row + x][end_col - x] == "*" or self._data[end_row - x][end_col + x] == "*":
                return False
        return True

    def _fire(self, row, col):
        end_row, end_col = self._get_position_of_endeavour()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not self._on_board(end_row + i, end_col + j):
                    continue
                if self._data[row + i][col + j] == "B":
                    self._data[row + i][col + j] = " "
                    self._enemy_ship -= 1
                    self._place_enemy_ship()

                    return True
        return False




