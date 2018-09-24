import random
from src.Entity import Entity


# A class describing the game board
class Board:

    def __init__(self, w, h, bombs, side):
        self.w = w
        self.h = h
        self.side = side
        self.bombs = bombs
        self.bomb_matrix = []
        self.board_matrix = []
        self.opened_matrix = []

        for row in range(h):
            opened_row = []
            for column in range(w):
                opened_row.append(0)
            self.opened_matrix.append(opened_row)

        """
        # print opened_matrix
        for row in range(h):
            print(self.opened_matrix[row])
        """

    def place_bombs(self):

        # Randomizes bombs
        cells = self.w * self.h
        bomb_pos_list = random.sample(range(0, cells), self.bombs)
        bomb_pos_list.sort()

        # Places the bombs on the board
        current_bomb = 0
        self.bomb_matrix = []
        for row in range(self.h):
            bomb_row = []
            for column in range(self.w):
                cell = row * self.w + column
                bomb = 0
                if not current_bomb == self.bombs:
                    if cell == bomb_pos_list[current_bomb]:
                        bomb = 9
                        current_bomb += 1
                bomb_row.append(bomb)
            self.bomb_matrix.append(bomb_row)

        # Calculates the board
        self.board_matrix = []
        for row in range(self.h):
            board_row = []
            for column in range(self.w):
                current_cell = self.bomb_matrix[row][column]
                if current_cell != 9:
                    lookup = get_neighbors(self.bomb_matrix, row, column)
                    neighboring_bombs = count_neighbor_bombs(row, column, self.bomb_matrix, lookup)
                    appendix = neighboring_bombs
                else:
                    appendix = 9
                board_row.append(appendix)
            self.board_matrix.append(board_row)

    def print_bomb(self):

        print("\nBomb Matrix:\n")
        for row in self.bomb_matrix:
            print(row)

    def print_board(self):

        print("\nBoard Matrix:\n")
        for r in self.board_matrix:
            print(r)

    def draw(self, screen):
        e = Entity("../resources/tiles/XS/0.png", 0, 0, self.side, self.side)
        e1 = Entity("../resources/tiles/XS/1.png", 0, 0, self.side, self.side)
        e2 = Entity("../resources/tiles/XS/2.png", 0, 0, self.side, self.side)
        e3 = Entity("../resources/tiles/XS/3.png", 0, 0, self.side, self.side)
        e4 = Entity("../resources/tiles/XS/4.png", 0, 0, self.side, self.side)
        e5 = Entity("../resources/tiles/XS/5.png", 0, 0, self.side, self.side)
        e6 = Entity("../resources/tiles/XS/6.png", 0, 0, self.side, self.side)
        e7 = Entity("../resources/tiles/XS/7.png", 0, 0, self.side, self.side)
        e8 = Entity("../resources/tiles/XS/8.png", 0, 0, self.side, self.side)
        e9 = Entity("../resources/tiles/XS/b.png", 0, 0, self.side, self.side)
        y = 0
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                cell = self.board_matrix[row][column]
                if cell == 0:
                    e.update(x, y)
                    e.draw(screen)
                elif cell == 1:
                    e1.update(x, y)
                    e1.draw(screen)
                elif cell == 2:
                    e2.update(x, y)
                    e2.draw(screen)
                elif cell == 3:
                    e3.update(x, y)
                    e3.draw(screen)
                elif cell == 4:
                    e4.update(x, y)
                    e4.draw(screen)
                elif cell == 5:
                    e5.update(x, y)
                    e5.draw(screen)
                elif cell == 6:
                    e6.update(x, y)
                    e6.draw(screen)
                elif cell == 7:
                    e7.update(x, y)
                    e7.draw(screen)
                elif cell == 8:
                    e8.update(x, y)
                    e8.draw(screen)
                elif cell == 9:
                    e9.update(x, y)
                    e9.draw(screen)
                x += self.side
            y += self.side

    def draw_start(self, screen):
        y = 0
        x = 0
        e = Entity("../resources/tiles/XS/u.png", x, y, self.side, self.side)
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                e.update(x, y)
                e.draw(screen)
                x += self.side
            y += self.side

    def calculate_screen_res(self):
        return [self.side * self.w, self.side * self.h]


# Returns a lookup matrix for neighboring cells.
def get_neighbors(matrix, x, y):
    h = len(matrix) - 1
    w = len(matrix[0]) - 1

    if x == 0 and y == 0:
        lookup = [[0, 0, 0],
                  [0, 1, 1],
                  [0, 1, 1]]
    elif x == 0 and y != 0 and y != w:
        lookup = [[0, 0, 0],
                  [1, 1, 1],
                  [1, 1, 1]]
    elif x == 0 and y == w:
        lookup = [[0, 0, 0],
                  [1, 1, 0],
                  [1, 1, 0]]
    elif x != 0 and x != h and y == w:
        lookup = [[1, 1, 0],
                  [1, 1, 0],
                  [1, 1, 0]]
    elif x == h and y == w:
        lookup = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 0]]
    elif x == h and y != 0 and y != w:
        lookup = [[1, 1, 1],
                  [1, 1, 1],
                  [0, 0, 0]]
    elif x == h and y == 0:
        lookup = [[0, 1, 1],
                  [0, 1, 1],
                  [0, 0, 0]]
    elif x != 0 and x != h and y == 0:
        lookup = [[0, 1, 1],
                  [0, 1, 1],
                  [0, 1, 1]]
    else:
        lookup = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]

    return lookup


# Counts the neighbors which are bombs
def count_neighbor_bombs(x, y, matrix, lookup):
    bombs = 0

    coordinates = [[[-1, -1], [-1, 0], [-1, 1]],
                   [[0, -1], [0, 0], [0, 1]],
                   [[1, -1], [1, 0], [1, 1]]]

    for row in range(3):
        for column in range(3):
            if lookup[row][column] == 1:
                look = coordinates[row][column]
                x_p = x + look[0]
                y_p = y + look[1]
                if matrix[x_p][y_p] == 9:
                    bombs += 1

    return bombs


"""
if __name__ == "__main__":
    board = Board(10, 9, 10)
    board.place_bombs()
"""