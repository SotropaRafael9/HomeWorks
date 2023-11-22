#make me a implementation of scramble game
import math
import random
import sys
class Game:
    def __init__(self, size_x, size_y) -> None:
        self.size = [size_x, size_y]
        self.matrix = []
        self.empty = [0, 0]
        self.moves = 0
        self.init_matrix()

    def init_matrix(self) -> None:
        for pos_x in range(self.size[0]):
            self.matrix.append([])
            for pos_y in range(self.size[1]):
                self.matrix[pos_x].append(pos_x * self.size[1] + pos_y + 1)
        self.matrix[self.size[0] - 1][self.size[1] - 1] = 0
        self.empty = [self.size[0] - 1, self.size[1] - 1]

    def __str__(self) -> str:
        result = ""
        for pos_x in range(self.size[0]):
            for pos_y in range(self.size[1]):
                result += str(self.matrix[pos_x][pos_y]) + " "
            result += "\n"
        return result

    def move(self, pos_x, pos_y) -> bool:
        if pos_x < 0 or pos_y < 0 or self.size[0] <= pos_x or self.size[1] <= pos_y:
            return False
        if abs(self.empty[0] - pos_x) + abs(self.empty[1] - pos_y) != 1:
            return False
        self.matrix[self.empty[0]][self.empty[1]] = self.matrix[pos_x][pos_y]
        self.matrix[pos_x][pos_y] = 0
        self.empty = [pos_x, pos_y]
        self.moves += 1
        return True

    def is_solved(self) -> bool:
        for pos_x in range(self.size[0]):
            for pos_y in range(self.size[1]):
                if self.matrix[pos_x][pos_y] != pos_x * self.size[1] + pos_y + 1:
                    return False
        return True

    def shuffle(self, moves) -> None:
        for i in range(moves):
            while True:
                pos_x = self.empty[0] + random.randint(-1, 1)
                pos_y = self.empty[1] + random.randint(-1, 1)
                if self.move(pos_x, pos_y):
                    break

    def solve(self) -> None:
        self.init_matrix()
        self.shuffle(100)
        while not self.is_solved():
            self.move(self.empty[0] + random.randint(-1, 1), self.empty[1] + random.randint(-1, 1))

    def get_moves(self) -> int:
        return self.moves

    def get_matrix(self) -> list:
        return self.matrix

    def get_empty(self) -> list:
        return self.empty

    def get_size(self) -> list:
        return self.size

    def get_size_x(self) -> int:
        return self.size[0]

    def get_size_y(self) -> int:
        return self.size[1]

    def get_value(self, pos_x, pos_y) -> int:
        return self.matrix[pos_x][pos_y]

    def set_value(self, pos_x, pos_y, value) -> None:
        self.matrix[pos_x][pos_y] = value

    def set_empty(self, pos_x, pos_y) -> None:
        self.empty = [pos_x, pos_y]

    def set_size(self, size_x, size_y) -> None:
        self.size = [size_x, size_y]

    def set_size_x(self, size_x) -> None:
        self.size[0] = size_x

    def set_size_y(self, size_y) -> None:
        self.size[1] = size_y

    def set_moves(self, moves) -> None:
        self.moves = moves

    def set_matrix(self, matrix) -> None:
        self.matrix = matrix

    def __eq__(self, other) -> bool:
        if self.size != other.size:
            return False
        if self.matrix != other.matrix:
            return False
        if self.empty != other.empty:
            return False
        if self.moves != other.moves:
            return False
        return True

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        return self.moves < other.moves

    def __le__(self, other) -> bool:
        return self.moves <= other.moves

    def __gt__(self, other) -> bool:
        return self.moves > other.moves

    def __ge__(self, other) -> bool:
        return self.moves >= other.moves

    def __add__(self, other) -> int:
        return self.moves + other.moves

    def __sub__(self, other) -> int:
        return self.moves - other.moves

    def __mul__(self, other) -> int:
        return self.moves * other.moves

    def __truediv__(self, other) -> int:
        return self.moves / other.moves

    def __floordiv__(self, other) -> int:
        return self.moves // other.moves   

    def __mod__(self, other) -> int:
        return self.moves % other.moves

    def __pow__(self, other) -> int:
        return self.moves ** other.moves

    def __and__(self, other) -> int:
        return self.moves & other.moves

    def __xor__(self, other) -> int:
        return self.moves ^ other.moves

    def __or__(self, other) -> int:
        return self.moves | other.moves

    def __lshift__(self, other) -> int:
        return self.moves << other.moves

    def __rshift__(self, other) -> int:
        return self.moves >> other.moves

    def __iadd__(self, other) -> int:
        self.moves += other.moves
        return self.moves

    def __isub__(self, other) -> int:
        self.moves -= other.moves
        return self.moves

    def __imul__(self, other) -> int:

        self.moves *= other.moves
        return self.moves

    def __itruediv__(self, other) -> int:
        self.moves /= other.moves
        return self.moves

    def __ifloordiv__(self, other) -> int:
        self.moves //= other.moves
        return self.moves

    def __imod__(self, other) -> int:
        self.moves %= other.moves
        return self.moves

    def __ipow__(self, other) -> int:
        self.moves **= other.moves
        return self.moves

    def __iand__(self, other) -> int:
        self.moves &= other.moves
        return self.moves

    def __ixor__(self, other) -> int:
        self.moves ^= other.moves
        return self.moves

    def __ior__(self, other) -> int:
        self.moves |= other.moves
        return self.moves

    def __ilshift__(self, other) -> int:
        self.moves <<= other.moves
        return self.moves

    def __irshift__(self, other) -> int:
        self.moves >>= other.moves
        return self.moves

    def __neg__(self) -> int:
        return -self.moves

    def __pos__(self) -> int:
        return +self.moves

    def __abs__(self) -> int:
        return abs(self.moves)

    def __invert__(self) -> int:
        return ~self.moves

    def __round__(self, n=None) -> int:
        return round(self.moves, n)

    def __trunc__(self) -> int:
        return math.trunc(self.moves)

    def __floor__(self) -> int:
        return math.floor(self.moves)

    def __ceil__(self) -> int:
        return math.ceil(self.moves)

    def __index__(self) -> int:
        return self.moves

    def __hash__(self) -> int:
        return hash(self.moves)

    def __str__(self) -> str:
        return str(self.moves)

    def __repr__(self) -> str:
        return repr(self.moves)

    def __format__(self, format_spec) -> str:
        return format(self.moves, format_spec)

    def __sizeof__(self) -> int:
        return sys.getsizeof(self.moves)

class Puzzle:

    def __init__(self, matrix, size_x, size_y, empty_x, empty_y):
        self.matrix = matrix
        self.size_x = size_x
        self.size_y = size_y
        self.empty_x = empty_x
        self.empty_y = empty_y

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return repr(self.matrix)

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __ne__(self, other):
        return self.matrix != other.matrix

    def __lt__(self, other):
        return self.matrix < other.matrix

    def __le__(self, other):
        return self.matrix <= other.matrix

    def __gt__(self, other):
        return self.matrix > other.matrix

    def __ge__(self, other):
        return self.matrix >= other.matrix

    def __add__(self, other):
        return self.matrix + other.matrix

    def __sub__(self, other):
        return self.matrix - other.matrix

    def __mul__(self, other):
        return self.matrix * other.matrix

    def __truediv__(self, other):
        return self.matrix / other.matrix

    def __floordiv__(self, other):
        return self.matrix // other.matrix

    def __mod__(self, other):
        return self.matrix % other.matrix

    def __pow__(self, other):
        return self.matrix ** other.matrix

    def __and__(self, other):
        return self.matrix & other.matrix

    def __xor__(self, other):
        return self.matrix ^ other.matrix

    def __or__(self, other):
        return self.matrix | other.matrix

    def __lshift__(self, other):
        return self.matrix << other.matrix

    def __rshift__(self, other):
        return self.matrix >> other.matrix

    def __iadd__(self, other):
        self.matrix += other.matrix
        return self.matrix

    def __isub__(self, other):
        self.matrix -= other.matrix
        return self.matrix

    def __imul__(self, other):
        self.matrix *= other.matrix
        return self.matrix

    def __itruediv__(self, other):
        self.matrix /= other.matrix
        return self.matrix

    def __ifloordiv__(self, other):
        self.matrix //= other.matrix
        return self.matrix

    def __imod__(self, other):
        self.matrix %= other.matrix
        return self.matrix

    def __ipow__(self, other):
        self.matrix **= other.matrix
        return self.matrix

    def __iand__(self, other):
        self.matrix &= other.matrix
        return self.matrix

    def __ixor__(self, other):
        self.matrix ^= other.matrix
        return self.matrix

    def __ior__(self, other):
        self.matrix |= other.matrix
        return self.matrix

    def __ilshift__(self, other):

        self.matrix <<= other.matrix
        return self.matrix

    def __irshift__(self, other):
        self.matrix >>= other.matrix
        return self.matrix

    def __neg__(self):
        return -self.matrix

    def __pos__(self):
        return +self.matrix
        








