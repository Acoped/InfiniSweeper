import random
from game.matrix import *
from game.Entity import Entity
from copy import copy, deepcopy

# A class describing the game board
class Board:

    def __init__(self, w, h, bombs, side, increased_border : bool = False):

        self.screen = None          # Define later in set_screen! Which screen to draw to.
        self.w = w                  # Width of the Board in tiles.
        self.h = h                  # Height of the Board in tiles
        self.side = side            # Side of a tile in pixels
        self.bombs = bombs          # Number of bombs
        self.increased_border = increased_border      # Whether increased increased_border is selected or not
        self.cells_opened = 0       # number of opened cells
        self.lose = False           # if game is lost or not
        self.win = False            # if game is won or not
        self.last_held = [None, None] # last held down tile

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

        self.set_entities(side)

    # Sets the 'Entity' or texture for the squares, based on chosen resolution
    def set_entities(self, side_in_px):

        if self.increased_border:
            if side_in_px < 128:
                self.e = Entity("../resources/tiles/increased_border/L/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/increased_border/L/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/increased_border/L/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/increased_border/L/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/increased_border/L/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/increased_border/L/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/increased_border/L/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/increased_border/L/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/increased_border/L/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/increased_border/L/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/increased_border/L/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/increased_border/L/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/increased_border/L/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/increased_border/L/u.png", 0, 0, self.side, self.side)
            if side_in_px < 64:
                self.e = Entity("../resources/tiles/increased_border/M/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/increased_border/M/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/increased_border/M/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/increased_border/M/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/increased_border/M/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/increased_border/M/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/increased_border/M/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/increased_border/M/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/increased_border/M/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/increased_border/M/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/increased_border/M/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/increased_border/M/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/increased_border/M/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/increased_border/M/u.png", 0, 0, self.side, self.side)
            if side_in_px < 32:
                self.e = Entity("../resources/tiles/increased_border/S/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/increased_border/S/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/increased_border/S/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/increased_border/S/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/increased_border/S/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/increased_border/S/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/increased_border/S/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/increased_border/S/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/increased_border/S/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/increased_border/S/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/increased_border/S/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/increased_border/S/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/increased_border/S/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/increased_border/S/u.png", 0, 0, self.side, self.side)
            if side_in_px < 16:
                self.e = Entity("../resources/tiles/increased_border/XS/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/increased_border/XS/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/increased_border/XS/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/increased_border/XS/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/increased_border/XS/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/increased_border/XS/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/increased_border/XS/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/increased_border/XS/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/increased_border/XS/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/increased_border/XS/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/increased_border/XS/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/increased_border/XS/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/increased_border/XS/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/increased_border/XS/u.png", 0, 0, self.side, self.side)
            if side_in_px < 8:
                self.e = Entity("../resources/tiles/increased_border/XXS/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/increased_border/XXS/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/increased_border/XXS/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/increased_border/XXS/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/increased_border/XXS/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/increased_border/XXS/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/increased_border/XXS/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/increased_border/XXS/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/increased_border/XXS/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/increased_border/XXS/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/increased_border/XXS/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/increased_border/XXS/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/increased_border/XXS/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/increased_border/XXS/u.png", 0, 0, self.side, self.side)
        else:
            if side_in_px < 128:
                self.e = Entity("../resources/tiles/standard/L/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/standard/L/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/standard/L/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/standard/L/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/standard/L/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/standard/L/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/standard/L/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/standard/L/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/standard/L/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/standard/L/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/standard/L/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/standard/L/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/standard/L/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/standard/L/u.png", 0, 0, self.side, self.side)
            if side_in_px < 64:
                self.e = Entity("../resources/tiles/standard/M/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/standard/M/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/standard/M/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/standard/M/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/standard/M/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/standard/M/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/standard/M/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/standard/M/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/standard/M/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/standard/M/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/standard/M/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/standard/M/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/standard/M/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/standard/M/u.png", 0, 0, self.side, self.side)
            if side_in_px < 32:
                self.e = Entity("../resources/tiles/standard/S/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/standard/S/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/standard/S/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/standard/S/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/standard/S/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/standard/S/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/standard/S/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/standard/S/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/standard/S/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/standard/S/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/standard/S/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/standard/S/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/standard/S/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/standard/S/u.png", 0, 0, self.side, self.side)
            if side_in_px < 16:
                self.e = Entity("../resources/tiles/standard/XS/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/standard/XS/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/standard/XS/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/standard/XS/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/standard/XS/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/standard/XS/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/standard/XS/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/standard/XS/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/standard/XS/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/standard/XS/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/standard/XS/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/standard/XS/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/standard/XS/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/standard/XS/u.png", 0, 0, self.side, self.side)
            if side_in_px < 8:
                self.e = Entity("../resources/tiles/standard/XXS/0.png", 0, 0, self.side, self.side)
                self.e1 = Entity("../resources/tiles/standard/XXS/1.png", 0, 0, self.side, self.side)
                self.e2 = Entity("../resources/tiles/standard/XXS/2.png", 0, 0, self.side, self.side)
                self.e3 = Entity("../resources/tiles/standard/XXS/3.png", 0, 0, self.side, self.side)
                self.e4 = Entity("../resources/tiles/standard/XXS/4.png", 0, 0, self.side, self.side)
                self.e5 = Entity("../resources/tiles/standard/XXS/5.png", 0, 0, self.side, self.side)
                self.e6 = Entity("../resources/tiles/standard/XXS/6.png", 0, 0, self.side, self.side)
                self.e7 = Entity("../resources/tiles/standard/XXS/7.png", 0, 0, self.side, self.side)
                self.e8 = Entity("../resources/tiles/standard/XXS/8.png", 0, 0, self.side, self.side)
                self.e9 = Entity("../resources/tiles/standard/XXS/b.png", 0, 0, self.side, self.side)
                self.br = Entity("../resources/tiles/standard/XXS/br.png", 0, 0, self.side, self.side)
                self.f = Entity("../resources/tiles/standard/XXS/f.png", 0, 0, self.side, self.side)
                self.q = Entity("../resources/tiles/standard/XXS/q.png", 0, 0, self.side, self.side)
                self.u = Entity("../resources/tiles/standard/XXS/u.png", 0, 0, self.side, self.side)
                
    def set_screen(self, screen):
        self.screen = screen

    # Can be used for multiplayer
    def construct_from_board_matrix(self):
        pass

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
                    neighboring_bombs = self.count_neighbor_bombs(row, column, self.bomb_matrix, lookup)
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
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in A]))

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
        field = self.island_matrix[y][x]
        return field

    # Opens the zero field
    def open_zero_field(self, field):
        cells_to_open = self.lookup_matrix[field - 1]

        for coord in cells_to_open:
            x = coord[0]
            y = coord[1]
            self.open_tile_from_coords(y, x, False)

    def open_tile_from_mouse(self, mouse_pos):
        x, y = self.get_clicked_tile(mouse_pos)
        should_multiplayer_update = self.open_tile_from_coords(x,y)
        return should_multiplayer_update

    def double_open_tile_from_mouse(self, mouse_pos):
        x, y = self.get_clicked_tile(mouse_pos)
        flags = self.count_neighbor_flags(x, y, self.flag_matrix)

        should_multiplayer_update = False
        if flags == self.board_matrix[y][x]:
            should_multiplayer_update = True
            self.open_cells_not_flagged(x, y)

        return should_multiplayer_update

    def open_cells_not_flagged(self, x, y):
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

        # This should probably be solved better, kind of an ugly fix...
        # ----- Sunken effect correcter -----
        """
        last_x = self.last_held[0]
        last_y = self.last_held[1]
        if last_x is not None and last_x != x and last_y != y:
            self.e8.update(last_x * self.side, last_y * self.side)
            self.e8.draw(self.screen)
        self.last_held = [None, None]
        """
        # ----- /Sunken effect correcter -----

        cell = self.board_matrix[y][x]

        should_multiplayer_update = False

        if self.opened_matrix[y][x] == 0 and self.flag_matrix[y][x] == 0:

            should_multiplayer_update = True

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
                self.game_lose()

            # Mark cells as opened or not accordingly and check for game over
            if not cell == 9:
                if self.opened_matrix[y][x] == 0:
                    self.opened_matrix[y][x] = 1
                    self.cells_opened += 1
            if self.w * self.h - self.bombs == self.cells_opened:
                if not self.lose:
                    self.game_won()

            # print('cells_open ', self.cells_opened)
            # self.print_open_matrix()

        return should_multiplayer_update

    def game_won(self):
        print("GAME WON!")
        self.win = True

    def game_lose(self):
        print("GAME LOST!")
        self.lose = True

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

    # Unhide this method later for "sunken effect" on held down unopened tiles
    """
    def draw_hold(self, mouse_pos):

        mx = mouse_pos[0]
        my = mouse_pos[1]

        x = int(mx / self.side)
        y = int(my / self.side)

        if self.opened_matrix[y][x] == 0 and self.flag_matrix[y][x] == 0:
            self.q.update(x * self.side, y * self.side)
            self.q.draw(self.screen)

        last_x = self.last_held[0]
        last_y = self.last_held[1]
        if last_x is not None:
            if not (x == last_x and y == last_y) and self.opened_matrix[last_y][last_x] == 0 and self.flag_matrix[last_y][last_x] == 0:
                self.e8.update(last_x * self.side, last_y * self.side)
                self.e8.draw(self.screen)

        print("N", x, y)
        print("L", last_x, last_y)

        self.last_held = [x, y]
    """

    def calculate_screen_res(self):
        return [self.side * self.w, self.side * self.h]

    def mark_from_mouse_pos(self, mouse_pos):
        x, y = self.get_clicked_tile(mouse_pos)
        should_multiplayer_update = self.mark(x, y)

        return should_multiplayer_update

    def mark(self, x, y):

        should_multiplayer_update = False

        xd = x * self.side
        yd = y * self.side

        # if not opened
        if self.opened_matrix[y][x] == 0:
            should_multiplayer_update = True
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

        return should_multiplayer_update


    # Counts the neighbors which are bombs
    def count_neighbor_bombs(self, x, y, matrix, lookup):
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


    def count_neighbor_flags(self, x, y, flag_matrix):

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
                    if (0 <= x_p <= self.w) and (0 <= y_p <= self.h):
                        if flag_matrix[y_p][x_p] == 1:
                            # print('flag_x', x_p, 'flag_y', y_p)
                            flags += 1
                except IndexError:
                    pass

        # print("neighboring flags: ", flags)

        return flags

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


"""
if __name__ == "__main__":
    board = Board(10, 9, 10)
    board.place_bombs()
"""