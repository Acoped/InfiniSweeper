from game import Board


class NewGamePacket:
    """
    A class representing new game (and restart) data to be sent or received for a multi-player game over a network
    """

    # (if 'board' is not supplied, a placeholder board that will NOT be used is created!!)
    def __init__(self, board: Board = Board(1, 1, 1, 1)):
        self.board: Board = board

    def __str__(self):
        return '\n----------\n'\
            'NewGamePacket object' + ' [side = ' + str(self.board.side) + ', increased_border = ' \
               + str(self.board.increased_border) + ']\n' \
               + 'board =\n' \
               + ('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in self.board.board_matrix])) \
               + '\n----------\n'

    def serialize(self) -> str:
        serialized = "0_" + str(self.board.side) + "_" + str(int(self.board.increased_border)) + "_"
        for x in range(self.board.h):
            serialized += "/"
            for y in range(self.board.w):
                serialized += str(self.board.board_matrix[x][y])

        return serialized

    def deserialize(self, message: str):
        message = message[2:]
        split = message.split("_")
        side = int(split[0])
        increased_border = int(split[1])
        message = split[2]

        print(message)

        matrix = []
        row = -1

        bombs = 0

        for c in message:
            if c == '/':
                row += 1
                matrix.append([])
            else:
                matrix[row].append(int(c))
                if c == '9':
                    bombs += 1

        w = len(matrix[0])
        h = len(matrix)

        self.board = Board(w, h, bombs, side, increased_border=bool(increased_border))
        self.board.board_matrix = matrix


# ----- Testing ----- (mbe write unit tests?)

# Sending
send_board = Board(5, 3, 3, 32, increased_border=True)
send_board.place_bombs()
send_board.print_board()
send_packet = NewGamePacket(send_board)
print(send_packet)

# Receiving
received_message = send_packet.serialize()
print(received_message)
receive_packet = NewGamePacket()
print("received_message: ", received_message)
receive_packet.deserialize(received_message)
print(receive_packet)
