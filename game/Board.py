import random
from game.matrix import *
from game.Entity import Entity
from copy import copy, deepcopy

# A class describing the game board
class Board:

    def __init__(self, w, h, bombs, side):

        self.screen = None          # Define later in set_screen! Which screen to draw to.
        self.w = w                  # Width of the Board in tiles.
        self.h = h                  # Height of the Board in tiles
        self.side = side            # Side of a tile in pixels
        self.bombs = bombs          # Number of bombs

        self.bomb_matrix = []       # Binary matrix. If tile is bomb or not. Bomb is 1.
        self.board_matrix = []      # Integer matrix. Number of neighboring bombs 0-8. Bomb is 9.
        self.opened_matrix = []     # Binary matrix. If cell is opened or not. Opened is 1.
        self.island_matrix = []     # Integer matrix. ID's of connected "islands" of 0-fields.
        self.lookup_matrix = []     # Matrix with coordinates to the fields that should be opened when a 0 is clicked
        self.flag_matrix = []       # Binary matrix. If tile is marked with a flag or not. Flag is 1

        # Initiates opened_matrix
        for row in range(h):
            opened_row = []
            for column in range(w):
                opened_row.append(0)
            self.opened_matrix.append(opened_row)

        # Initiates flag_matrix
        for row in range(h):
            opened_row = []
            for column in range(w):
                opened_row.append(0)
            self.flag_matrix.append(opened_row)

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

    def set_screen(self, screen):
        self.screen = screen

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

    # Finds the 0-islands and id:s them.
    # Also creates a lookup table for 0-islands and cells neighboring 0-islands for efficient opening of 0-islands.
    def find_islands(self):

        # ----- FIND ISLANDS -----
        padding = 999999

        self.island_matrix = deepcopy(self.board_matrix)
        # self.print_island()

        self.island_matrix = change_all_except(self.island_matrix, -1, 0)
        # self.print_island()

        # Finds islands. Non-optimal solution.
        # Still, while only doing this once on startup, it's not that expensive.
        # The created look-up table for 0-islands makes up for the cost
        pad(self.island_matrix, padding)
        id = 0
        for i in range(self.h + 1):
            for j in range(self.w + 1):
                if self.island_matrix[i][j] == 0:
                    id += 1
                    self.fid(id, i, j)
        self.island_matrix = un_pad(self.island_matrix)

        # self.print_island()
        # print("\nFound ", id, " islands!")
        # ----- /FIND ISLANDS -----

        # ----- BELONGING TABLE -----
        # Creates a lookuptable of cells' neighboring islands
        c = [[[-1, -1], [-1, 0], [-1, 1]],
               [[0, -1], [0, 0], [0, 1]],
               [[1, -1], [1, 0], [1, 1]]]

        n_matrix = []

        # För varje cell
        self.island_matrix = pad(self.island_matrix, padding)
        for i in range(self.h + 2):
            n_row = []
            for j in range(self.w + 2):
                # om inte padding och -1
                cell = self.island_matrix[i][j]
                if cell!= padding:
                    # kolla alla grannar
                    n = []
                    for row in range(3):
                        for column in range(3):
                            look = c[row][column]
                            x_p = i + look[0]
                            y_p = j + look[1]
                            check = self.island_matrix[x_p][y_p]
                            if check != -1 and check != padding and check not in n:
                                n.append(check)
                    n_row.append(n)
                else:
                    n_row.append([cell])
            n_matrix.append(n_row)
        self.island_matrix = un_pad(self.island_matrix)

        n_matrix = un_pad(n_matrix)

        # print("\nBelong to field matrix:\n")
        # for n_row in n_matrix:
        #     print(n_row)
        # ----- /BELONGING TABLE -----

        # ----- LOOKUP TABLE -----
        look_up_zero_fields = []

        for i in range(id):
            look_up_zero_fields.append([])

        # för varje cell
        for i in range(self.h):
            for j in range(self.w):
                belong_to_list = n_matrix[i][j]
                # för varje element i listan för vilka 0-fält cellen tillhör
                for element in belong_to_list:
                    # ange koordinaterna till id:t på rätt plats
                    look_up_zero_fields[element - 1].append([i, j])

        """
        print("\nLookup field matrix\n")
        for row in look_up_zero_fields:
            print(row)
        """

        self.lookup_matrix = look_up_zero_fields
        # ----- /LOOKUP TABLE -----

    # find_islands_deep, recursive function
    def fid(self, id, x, y):
        if self.island_matrix[x][y] == 0:
            self.island_matrix[x][y] = id
            self.fid(id, x + 1, y)
            self.fid(id, x, y + 1)
            self.fid(id, x - 1, y)
            self.fid(id, x, y - 1)
            self.fid(id, x + 1, y + 1)
            self.fid(id, x - 1, y - 1)
            self.fid(id, x + 1, y - 1)
            self.fid(id, x - 1, y + 1)

    def print_island(self):
        print("\nIsland Matrix:\n")

        sea_before = -1
        sea_after = "~"  # Unicode for black square

        print_island_matrix = [["   " + sea_after if x == sea_before else x for x in row] for row in self.island_matrix]

        self.nice_print(print_island_matrix)

    def nice_print(self, A):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in A]))

    def print_bomb(self):
        print("\nBomb Matrix:\n")
        self.nice_print(self.bomb_matrix)

    def print_board(self):
        print("\nBoard Matrix:\n")
        self.nice_print(self.board_matrix)

    def print_open_matrix(self):
        print("\nOpened Matrix:\n")
        self.nice_print(self.opened_matrix)

    def print_flag_matrix(self):
        print("\nFlag Matrix:\n")
        self.nice_print(self.flag_matrix)

    def draw(self):
        y = 0
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                cell = self.board_matrix[row][column]
                if cell == 0:
                    self.e.update(x, y)
                    self.e.draw(self.screen)
                elif cell == 1:
                    self.e1.update(x, y)
                    self.e1.draw(self.screen)
                elif cell == 2:
                    self.e2.update(x, y)
                    self.e2.draw(self.screen)
                elif cell == 3:
                    self.e3.update(x, y)
                    self.e3.draw(self.screen)
                elif cell == 4:
                    self.e4.update(x, y)
                    self.e4.draw(self.screen)
                elif cell == 5:
                    self.e5.update(x, y)
                    self.e5.draw(self.screen)
                elif cell == 6:
                    self.e6.update(x, y)
                    self.e6.draw(self.screen)
                elif cell == 7:
                    self.e7.update(x, y)
                    self.e7.draw(self.screen)
                elif cell == 8:
                    self.e8.update(x, y)
                    self.e8.draw(self.screen)
                elif cell == 9:
                    self.e9.update(x, y)
                    self.e9.draw(self.screen)
                x += self.side
            y += self.side

    def draw_start(self):
        y = 0
        for row in range(self.h):
            x = 0
            for column in range(self.w):
                self.u.update(x, y)
                self.u.draw(self.screen)
                x += self.side
            y += self.side

    def get_clicked_tile(self, mouse_pos):
        mx = mouse_pos[0]
        my = mouse_pos[1]

        x = int(mx / self.side)
        y = int(my / self.side)

        return x, y

    # Gets the ID of the clicked zero field
    def get_zero_field(self, x, y):

        # print("get zero field", x, y)

        field = self.island_matrix[y][x]

        # print(field)

        return field

    # Opens the zero field
    def open_zero_field(self, field):
        cells_to_open = self.lookup_matrix[field - 1]

        for coord in cells_to_open:
            x = coord[0]
            y = coord[1]
            # print(coord)
            self.open_tile_from_coords(y, x, False)

    def open_tile_from_mouse(self, mouse_pos):
        x, y = self.get_clicked_tile(mouse_pos)
        self.open_tile_from_coords(x,y)

    def double_open_tile_from_mouse(self, mouse_pos):
        x, y = self.get_clicked_tile(mouse_pos)
        flags = count_neighbor_flags(x, y, self.flag_matrix)
        print(flags)


        if flags == self.board_matrix[y][x]:
            self.open_cells_not_flagged(x, y)

    def open_cells_not_flagged(self, x, y):
        print("OPEN CELLS NOT FLAGGED")
        lookup = get_neighbors(self.board_matrix, x, y)

        coordinates = [[[-1, -1], [-1, 0], [-1, 1]],
                       [[0, -1], [0, 0], [0, 1]],
                       [[1, -1], [1, 0], [1, 1]]]

        # ---- TEST ---
        """
        self.print_board()
        print('w', w, 'h', h)
        """
        # ---- /TEST ---

        w = len(self.board_matrix[0])
        h = len(self.board_matrix)


        for row in range(3):
            for column in range(3):
                look = coordinates[row][column]
                x_p = x + look[0]
                y_p = y + look[1]

                # if-sats här som kontrollerar att rutan inte 'går runt' planen
                if x_p >= 0 and x_p <= w and y_p >= 0 and y_p <= h:
                    try:
                        if self.flag_matrix[y_p][x_p] != 1:
                            self.open_tile_from_coords(x_p, y_p)
                            # print('o', x_p, y_p) # test
                    except IndexError:
                        pass

    def open_tile_from_coords(self, x, y, open_zero_field=True):

        cell = self.board_matrix[y][x]

        if self.opened_matrix[y][x] == 0 and self.flag_matrix[y][x] == 0:

            xd = x * self.side
            yd = y * self.side

            if cell == 0:
                self.e.update(xd, yd)
                if open_zero_field:
                    field = self.get_zero_field(x, y)
                    self.open_zero_field(field)
                self.e.draw(self.screen)
            elif cell == 1:
                self.e1.update(xd, yd)
                self.e1.draw(self.screen)
            elif cell == 2:
                self.e2.update(xd, yd)
                self.e2.draw(self.screen)
            elif cell == 3:
                self.e3.update(xd, yd)
                self.e3.draw(self.screen)
            elif cell == 4:
                self.e4.update(xd, yd)
                self.e4.draw(self.screen)
            elif cell == 5:
                self.e5.update(xd, yd)
                self.e5.draw(self.screen)
            elif cell == 6:
                self.e6.update(xd, yd)
                self.e6.draw(self.screen)
            elif cell == 7:
                self.e7.update(xd, yd)
                self.e7.draw(self.screen)
            elif cell == 8:
                self.e8.update(xd, yd)
                self.e8.draw(self.screen)
            elif cell == 9:
                self.draw_bombs(xd, yd)

            # todo: finish this
            # Mark cells as opened or not accordingly and check for game over
            if cell == 0:
                self.opened_matrix[y][x] = 1
                # pass
            elif cell == 9:
                pass
            else:
                self.opened_matrix[y][x] = 1

        # self.print_open_matrix()

    def draw_bombs(self, x, y):
        # todo: draw flags

        # draws the rest of the bombs
        by = 0
        for row in range(self.h):
            bx = 0
            for column in range(self.w):
                cell = self.board_matrix[row][column]
                if cell == 9:
                    self.e9.update(bx, by)
                    self.e9.draw(self.screen)
                bx += self.side
            by += self.side

        # draws the red clicked bombed
        self.br.update(x, y)
        self.br.draw(self.screen)

    """
    # Unhide this method later for "sunken effect" on held down unopened tiles
    def draw_hold(self, mouse_pos):

        mx = mouse_pos[0]
        my = mouse_pos[1]

        x = int(mx / self.side)
        y = int(my / self.side)
        print(x, y)

        if self.opened_matrix[y][x] == 0:
            self.e.update(x * self.side, y * self.side)
            self.e.draw(self.screen)
    """

    def calculate_screen_res(self):
        return [self.side * self.w, self.side * self.h]

    def mark_from_mouse_pos(self, mouse_pos):
        x, y = self.get_clicked_tile(mouse_pos)
        self.mark(x, y)

    def mark(self, x, y):

        xd = x * self.side
        yd = y * self.side

        # if not opened
        if self.opened_matrix[y][x] == 0:
            # if not flagged
            if self.flag_matrix[y][x] == 0:
                self.f.update(xd, yd)
                self.f.draw(self.screen)
                self.flag_matrix[y][x] = 1
            # if flagged
            elif self.flag_matrix[y][x] == 1:
                self.u.update(xd, yd)
                self.u.draw(self.screen)
                self.flag_matrix[y][x] = 0

        # self.print_flag_matrix()


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


def count_neighbor_flags(x, y, flag_matrix):

    flags = 0
    coordinates = [[[-1, -1], [-1, 0], [-1, 1]],
                   [[0, -1], [0, 0], [0, 1]],
                   [[1, -1], [1, 0], [1, 1]]]

    for row in range(3):
        for column in range(3):
            look = coordinates[row][column]
            x_p = x + look[0]
            y_p = y + look[1]
            try:
                if flag_matrix[y_p][x_p] == 1:
                    flags += 1
            except IndexError:
                pass

    return flags

"""
if __name__ == "__main__":
    board = Board(10, 9, 10)
    board.place_bombs()
"""