from game import Board


class NewGamePacket:
    """ A class representing new game (and restart) data to be sent or received for a multiplayer game over a network"""

    def __init__(self, board: Board):
        self.board = board

    def __str__(self):
        self.board.print_board()

    def serialize(self) -> str:
        return "0_"

    def deserializer(self, message: str):
        pass
