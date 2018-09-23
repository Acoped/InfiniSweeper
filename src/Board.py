import random

# A class describing the game board
class Board:

    def __init__(self, w, h, bombs):
        self.w = w
        self.h = h
        self.bombs = bombs
        self.bomb_matrix = []
        self.board_matrix = []

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
        self.board_matrix = self.bomb_matrix.copy()
        for row in range(self.h):
            for column in range(self.w):
                if self.board_matrix[row][column] != 9:
                    neighboring_bombs = 0


    def print(self):

        print("\nBomb Matrix:\n")
        for row in self.bomb_matrix:
            print(row)

        print("\nBoard Matrix:\n")
        for row in self.board_matrix:
            print(row)


def get_neighbors(matrix, x, y):
    h = len(matrix) - 1
    w = len(matrix[0]) - 1
    lookup = []

    if x == 0 and y == 0:
        lookup = [[0, 0, 0],
                  [0, 1, 1],
                  [0, 1, 1]]
    elif x != 0 != w and y == 0:
        lookup = [[0, 0, 0],
                  [1, 1, 1],
                  [1, 1, 1]]
    elif x == w and y == 0:
        lookup = [[0, 0, 0],
                  [1, 1, 0],
                  [1, 1, 0]]
    elif x == w and y != 0 != h:
        lookup = [[1, 1, 0],
                  [1, 1, 0],
                  [1, 1, 0]]
    elif x == w and y == h:
        lookup = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 0]]
    elif x != 0 != w and y == h:
        lookup = [[1, 1, 1],
                  [1, 1, 1],
                  [0, 0, 0]]
    elif x == 0 and y == h:
        lookup = [[0, 1, 1],
                  [0, 1, 1],
                  [0, 0, 0]]
    elif x == 0 and y != 0 != h:
        lookup = [[0, 1, 1],
                  [0, 1, 1],
                  [0, 1, 1]]
    else:
        lookup = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]



if __name__ == "__main__":
    board = Board(10, 9, 10)
    board.place_bombs()
    board.print()
