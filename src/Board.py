import random


# A class describing the game board
class Board:

    def __init__(self, w, h, bombs):
        self.w = w
        self.h = h
        self.bombs = bombs
        self.bomb_matrix = []

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
                        bomb = 1
                        current_bomb += 1
                bomb_row.append(bomb)
            self.bomb_matrix.append(bomb_row)

    def print(self):

        print("\nBomb Matrix:\n")
        for row in self.bomb_matrix:
            print(row)

        print("\nBoard:\n")


if __name__ == "__main__":
    board = Board(10, 9, 10)
    board.place_bombs()
    board.print()
