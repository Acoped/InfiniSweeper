import asyncio
from aioconsole import ainput
from networking import *
from game import Board


class GameServer:

    """
    def __init__(self, w, h, bombs, side, increased_border : bool = False):
        self.board = Board(w, h, bombs, side, increased_border)
    """

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
        server = await asyncio.start_server(self.handle_echo, '127.0.0.1', 8888)

        address = server.sockets[0].getsockname()
        print(f'Serving on {address}')

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    game_server = GameServer()
    asyncio.run(game_server.main())
