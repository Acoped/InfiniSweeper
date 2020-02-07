from game import Board


class NewGamePacket:
    """
    A class representing new game (and restart) data to be sent or received for a multi-player game over a network
    """

    def __init__(self, board: Board):
        self.board: Board = board

    def __str__(self):
        self.board.print_board()

    def serialize(self) -> str:
        serialized = "0_"
        matrix = self.board.board_matrix
        w = len(matrix[0])
        h = len(matrix)

        for x in range(w):
            serialized += "/"
            for y in range(h):
                serialized += str(matrix[y][x])
                if not y == h - 1:
                    serialized += "_"

        return serialized

    def deserializer(self, message: str):
        pass


# Code for testing, mbe write unit tests?
test_board = Board(5, 3, 3, 32)
test_board.place_bombs()

send_packet = NewGamePacket(test_board)
# print(send_packet)
print(send_packet.serialize())