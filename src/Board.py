import random
from src.Entity import Entity
from pygame.locals import *
import numpy

# A class describing the game board
class Board:

    def __init__(self, w, h, bombs, side):
        self.w = w
        self.h = h
        self.bombs = bombs
        self.bomb_matrix = []
        self.board_matrix = []
        self.side = 8

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

        self.print_bomb()

        # Calculates the board
        self.board_matrix = []
        for row in range(self.h):
            board_row = []
            for column in range(self.w):
                current_cell = self.bomb_matrix[row][column]
                print(current_cell)
                if current_cell != 9:
                    lookup = get_neighbors(self.bomb_matrix, row, column)
                    neighboring_bombs = count_neighbor_bombs(row, column, self.bomb_matrix, lookup)
                    appendix = neighboring_bombs
                else:
                    appendix = 9
                print("appendix: ", appendix)
                board_row.append(appendix)
            self.board_matrix.append(board_row)
            self.print_board()

    def print_bomb(self):

        print("\nBomb Matrix:\n")
        for row in self.bomb_matrix:
            print(row)

    def print_board(self):

        print("\nBoard Matrix:\n")
        for r in self.board_matrix:
            print(r)

    def draw(self, screen):
        x = 0
        y = 0
        # self.entity_matrix = []
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                cell = self.board_matrix[row][column]
                e = Entity("../resources/tiles/XS/0.png", x, y, self.side, self.side)
                if cell == 1:
                    e = Entity("../resources/tiles/XS/1.png", x, y, self.side, self.side)
                elif cell == 2:
                    e = Entity("../resources/tiles/XS/2.png", x, y, self.side, self.side)
                elif cell == 3:
                    e = Entity("../resources/tiles/XS/3.png", x, y, self.side, self.side)
                elif cell == 4:
                    e = Entity("../resources/tiles/XS/4.png", x, y, self.side, self.side)
                elif cell == 5:
                    e = Entity("../resources/tiles/XS/5.png", x, y, self.side, self.side)
                elif cell == 6:
                    e = Entity("../resources/tiles/XS/6.png", x, y, self.side, self.side)
                elif cell == 7:
                    e = Entity("../resources/tiles/XS/7.png", x, y, self.side, self.side)
                elif cell == 8:
                    e = Entity("../resources/tiles/XS/8.png", x, y, self.side, self.side)
                elif cell == 9:
                    e = Entity("../resources/tiles/XS/b.png", x, y, self.side, self.side)
                e.draw(screen)
                x += self.side
            y += self.side

        # screen.blit(self.image, self.rect)

    def calculate_screen_res(self):
        return [self.side * self.w, self.side * self.h]


# Returns a lookup matrix for neighboring cells.
def get_neighbors(matrix, x, y):
    h = len(matrix) - 1
    w = len(matrix[0]) - 1

    print()
    print("hw: ", h, w)
    lookup = []

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

    for row in lookup:
        print(row)

    return lookup


# Counts the neighbors which are bombs
def count_neighbor_bombs(x, y, matrix, lookup):
    bombs = 0
    """
    coordinates = [[[-1, -1],[0, -1],[1, -1]],
                   [[-1, 0],[0, 0],[1, 0]],
                   [[-1, 1],[0, 1],[1, 1]]]
    """
    coordinates = [[[-1, -1], [-1, 0], [-1, 1]],
                   [[0, -1], [0, 0], [0, 1]],
                   [[1, -1], [1, 0], [1, 1]],]
    print("x y: ", x, y)
    print("matrix_dim: ", len(matrix), len(matrix[0]))
    for row in range(3):
        for column in range(3):
            if lookup[row][column] == 1:
                look = coordinates[row][column]
                x_p = x + look[0]
                y_p = y + look[1]
                print("look: ", look)
                print("look: ", x_p, y_p)
                if matrix[x_p][y_p] == 9:
                    bombs += 1

    print("bombs: ", bombs)

    return bombs


"""
if __name__ == "__main__":
    board = Board(10, 9, 10)
    board.place_bombs()
"""