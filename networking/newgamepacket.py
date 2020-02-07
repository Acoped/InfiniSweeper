from game import Board


class NewGamePacket:
    """
    A class representing new game (and restart) data to be sent or received for a multi-player game over a network
    """

    def __init__(self, board: Board = None):
        self.board: Board = board

    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(item) for item in row])for row in self.board.board_matrix])

    def serialize(self) -> str:
        serialized = "0_"
        for x in range(self.board.h):
            serialized += "/"
            for y in range(self.board.w):
                serialized += str(self.board.board_matrix[x][y])
                if not y == self.board.w - 1:
                    serialized += "_"

        return serialized

    def deserialize(self, message: str):
        message = message[2:]

        row = -1
        for c in message:
            if c == '/':
                row += 1
            elif c == '_':
                pass
            else:
                self.board.board_matrix[row].append(int(c))


# ----- Testing ----- (mbe write unit tests?)

# Sending

send_board = Board(5, 3, 3, 32)
send_board.place_bombs()
send_packet = NewGamePacket(send_board)
print(send_packet)
print(send_packet.serialize())


# Receiving
"""
recieved_message = "0_/0_2_9_2_0/0_3_9_3_0/0_2_9_2_0"
recieve_packet = NewGamePacket()
recieve_packet.deserialize(recieved_message)
print(recieved_message)
print(recieve_packet)
"""