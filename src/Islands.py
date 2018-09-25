from src.Board import Board


def main():
    print("hej")
    board = Board(30, 16, 99, 8)
    board.place_bombs()
    board.find_islands()
    # board.fatten_islands()

if __name__ == "__main__":
    main()
