import asyncio
from aioconsole import ainput
from networking import newgamepacket
from game import Board
import sys
# import ast

MAX_CHARACTERS = 100000

class GameServer:

    def __init__(self, w, h, bombs, side, increased_border: bool = False):
        self.board = Board(w, h, bombs, side, increased_border)
        self.board.place_bombs()

        self.board.print_board()    # prints the baord to check if it was correctly initialized

    async def some_coroutine(self):
        line = await ainput("input 'quit' to quit server\n")
        if line == 'quit':
            print("Q pressed")

    async def handle_client(self, reader, writer):
        data = await reader.read(MAX_CHARACTERS)
        received_message = data.decode()
        address = writer.get_extra_info('peername')

        print(f"Server received {received_message!r} from {address!r}")

        message_list = received_message.split('|')

        client_name = message_list[0]
        message = message_list[1]

        print(client_name, message)

        send_message = self.handle_request(client_name, message)

        # Send message if it wasn't a ClickPacket that was received.
        if send_message is not None:
            print(f"Server sends: {send_message!r} to {address!r}")
            writer.write(send_message.encode())
            await writer.drain()
        else:
            print("Server received ClickPacket")

        writer.close()
        print("Server closed the connection\n")

    def handle_request(self, client_name: str, client_message: str) -> str:

        type = client_message[0]
        print(f'Message type: {type}')

        # Cient sent an request to update game state
        if type == "u":
            answer = "Här kommer den uppdaterade gamestaten"
        # Client sent a ClickPacket
        elif type == "1" or type == "2" or type == "3":
            answer = None   # Do not send back an answer (just update gamestate)
        # Client sent a request to join a game
        elif type == "j":
            answer = newgamepacket.NewGamePacket(board=self.board).serialize()
        # Client sent an erroneous message
        else:
            answer = "Jag har tagit emot ditt meddelande, men förstod inte vad du sa"

        return answer

    async def main(self):
        server = await asyncio.start_server(self.handle_client, '127.0.0.1', 8903)

        address = server.sockets[0].getsockname()
        print(f'Serving on {address}')

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    # Prepares the string commands that were sent in to the correct format for the main function
    i = sys.argv[1:]
    print(i)
    print(int(i[0]), int(i[1]), int(i[2]), int(i[3]), bool(i[4]))
    game_server = GameServer(int(i[0]), int(i[1]), int(i[2]), int(i[3]), bool(i[4]))
    asyncio.run(game_server.main())
