import asyncio
from aioconsole import ainput
# from networking import *
from game import Board
import sys
# import ast


class GameServer:

    def __init__(self, w, h, bombs, side, increased_border: bool = False):
        self.board = Board(w, h, bombs, side, increased_border)
        self.board.place_bombs()

        self.board.print_board()    # prints the baord to check if it was correctly initialized

    async def some_coroutine(self):
        line = await ainput("input 'quit' to quit server\n")
        if line == 'quit':
            print("Q pressed")

    async def handle_echo(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        address = writer.get_extra_info('peername')

        print(f"Received {message!r} from {address!r}")

        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()

        print("Close the connection")
        writer.close()

    async def main(self):
        server = await asyncio.start_server(self.handle_echo, '127.0.0.1', 8890)

        address = server.sockets[0].getsockname()
        print(f'Serving on {address}')

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    # Prepares the string commands that were sent in to the correct format for the main function
    l = sys.argv[1:]
    print(l)
    print(int(l[0]), int(l[1]), int(l[2]), int(l[3]), bool(l[4]))
    game_server = GameServer(int(l[0]), int(l[1]), int(l[2]), int(l[3]), bool(l[4]))
    asyncio.run(game_server.main())
