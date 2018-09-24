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

        self.e = Entity("../resources/tiles/XS/0.png", 0, 0, self.side, self.side)
        self.e1 = Entity("../resources/tiles/XS/1.png", 0, 0, self.side, self.side)
        self.e2 = Entity("../resources/tiles/XS/2.png", 0, 0, self.side, self.side)
        self.e3 = Entity("../resources/tiles/XS/3.png", 0, 0, self.side, self.side)
        self.e4 = Entity("../resources/tiles/XS/4.png", 0, 0, self.side, self.side)
        self.e5 = Entity("../resources/tiles/XS/5.png", 0, 0, self.side, self.side)
        self.e6 = Entity("../resources/tiles/XS/6.png", 0, 0, self.side, self.side)
        self.e7 = Entity("../resources/tiles/XS/7.png", 0, 0, self.side, self.side)
        self.e8 = Entity("../resources/tiles/XS/8.png", 0, 0, self.side, self.side)
        self.e9 = Entity("../resources/tiles/XS/b.png", 0, 0, self.side, self.side)

        self.br = Entity("../resources/tiles/XS/br.png", 0, 0, self.side, self.side)
        self.f = Entity("../resources/tiles/XS/f.png", 0, 0, self.side, self.side)
        self.q = Entity("../resources/tiles/XS/q.png", 0, 0, self.side, self.side)
        self.u = Entity("../resources/tiles/XS/u.png", 0, 0, self.side, self.side)

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
        y = 0
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                cell = self.board_matrix[row][column]
                if cell == 0:
                    self.e.update(x, y)
                    self.e.draw(screen)
                elif cell == 1:
                    self.e1.update(x, y)
                    self.e1.draw(screen)
                elif cell == 2:
                    self.e2.update(x, y)
                    self.e2.draw(screen)
                elif cell == 3:
                    self.e3.update(x, y)
                    self.e3.draw(screen)
                elif cell == 4:
                    self.e4.update(x, y)
                    self.e4.draw(screen)
                elif cell == 5:
                    self.e5.update(x, y)
                    self.e5.draw(screen)
                elif cell == 6:
                    self.e6.update(x, y)
                    self.e6.draw(screen)
                elif cell == 7:
                    self.e7.update(x, y)
                    self.e7.draw(screen)
                elif cell == 8:
                    self.e8.update(x, y)
                    self.e8.draw(screen)
                elif cell == 9:
                    self.e9.update(x, y)
                    self.e9.draw(screen)
                x += self.side
            y += self.side

    def draw_start(self, screen):
        y = 0
        x = 0
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                self.u.update(x, y)
                self.u.draw(screen)
                x += self.side
            y += self.side

    def open_tile(self, screen, mouse_pos):

        mx = mouse_pos[0]
        my = mouse_pos[1]

        x = int(mx / self.side)
        y = int(my / self.side)

        cell = self.board_matrix[y][x]


        if self.opened_matrix[y][x] == 0:

            # todo: finish this
            # Mark cells as opened or not accordingly and check for game over
            if cell == 0:
                pass
            elif cell == 9:
                pass
            else:
                self.opened_matrix[y][x] == 1

            x *= self.side
            y *= self.side

            if cell == 0:
                self.e.update(x, y)
                self.e.draw(screen)
            elif cell == 1:
                self.e1.update(x, y)
                self.e1.draw(screen)
            elif cell == 2:
                self.e2.update(x, y)
                self.e2.draw(screen)
            elif cell == 3:
                self.e3.update(x, y)
                self.e3.draw(screen)
            elif cell == 4:
                self.e4.update(x, y)
                self.e4.draw(screen)
            elif cell == 5:
                self.e5.update(x, y)
                self.e5.draw(screen)
            elif cell == 6:
                self.e6.update(x, y)
                self.e6.draw(screen)
            elif cell == 7:
                self.e7.update(x, y)
                self.e7.draw(screen)
            elif cell == 8:
                self.e8.update(x, y)
                self.e8.draw(screen)
            elif cell == 9:

                # todo: draw flags

                # draws the rest of the bombs
                by = 0
                for row in range(self.h):
                    bx = 0
                    for column in range(self.w):
                        cell = self.board_matrix[row][column]
                        if cell == 9:
                            self.e9.update(bx, by)
                            self.e9.draw(screen)
                        bx += self.side
                    by += self.side

                # draws the red clicked bombed
                self.br.update(x, y)
                self.br.draw(screen)

    # Unhide this method later for "sunken effect" on held down unopened tiles
    """
    def draw_hold(self, screen, mouse_pos):

        mx = mouse_pos[0]
        my = mouse_pos[1]

        x = int(mx / self.side)
        y = int(my / self.side)
        print(x, y)

        if self.opened_matrix[y][x] == 0:
            self.e.update(x * self.side, y * self.side)
            self.e.draw(screen)

        pass
    """


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