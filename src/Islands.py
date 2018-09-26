from src.Board import Board


def main():
    print("hej")
    # board = Board(30, 30, 150, 8)
    # board = Board(30, 16, 99, 8)
    # board = Board(9, 10, 10, 8)
    board = Board(5, 5, 4, 6)
    board.place_bombs()
    board.find_islands()

if __name__ == "__main__":
    main()
