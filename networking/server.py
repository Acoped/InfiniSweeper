import asyncio
from aioconsole import ainput
from networking import newgamepacket, clickpacket
from game import Board
import sys
# import ast

MAX_CHARACTERS = 100000

class GameServer:

    def __init__(self, address: str, port: int, w, h, bombs, side, increased_border: bool = False):
        self.address = address
        self.port = port

        self.board = Board(w, h, bombs, side, increased_border)
        self.board.place_bombs()
        self.board.print_board()        # Prints the board to check if it was correctly initialized

        self.game_state_list = []       # A list with all the ClickPackets containing game state
        self.game_state_sender = []     # The sender of the game state (ClickPacket) in game_stat_list
        self.client_latest_update = {}  # A dictionary with client nicks and their latest received client_list index
        
    def print_clients(self):
        print(f'client_list: {self.client_latest_update}')

    def print_game_state_list(self):
        print(f'----- game_state_list (len {str(len(self.game_state_list))}) -----')
        for i in range(len(self.game_state_list)):
            print(self.game_state_sender[i], self.game_state_list[i])
        print(f'----- /game_state_list -----')

    async def some_coroutine(self):
        line = await ainput("input 'quit' to quit server\n")
        if line == 'quit':
            print("Q pressed")

    async def handle_client(self, reader, writer):
        data = await reader.read(MAX_CHARACTERS)
        received_message = data.decode()
        address = writer.get_extra_info('peername')

        # print(f"Server received {received_message!r} from {address!r}")

        message_list = received_message.split('|')

        client_name = message_list[0]
        message = message_list[1]

        # print(client_name, message)

        send_message = self.handle_request(client_name, message)

        if isinstance(send_message[0], clickpacket.ClickPacket):
            # print("JAG VILL VARA DIN")
            # Send all ClickPackets except last, with a splitting 'm' tag
            merged_message = ""
            sender_list = self.game_state_sender[-len(send_message):]
            print(client_name + "'s NEW state: " + str(self.client_latest_update[client_name]))
            print(f'sender_list {sender_list}')
            for i in range(1, len(send_message)):
                if sender_list[i] != client_name:
                    merged_message += send_message[i].serialize() + "m"
            if merged_message == "":
                merged_message = "0"
            self.print_game_state_list()
            print("sending to " + client_name + ": " + merged_message +"\n")
            writer.write(merged_message.encode())
            await writer.drain()
        else:
            # Send message if it wasn't a ClickPacket that was received.
            if send_message is not None:
                # print(f"Server sends: {send_message!r} to {address!r}")
                writer.write(send_message.encode())
                await writer.drain()
            else:
                # print("Server received ClickPacket")
                pass

        writer.close()
        # print("Server closed the connection\n")

    def handle_request(self, client_name: str, client_message: str):

        type = client_message[0]
        # print(f'Message type: {type}')

        # Cient sent an request to update game state
        if type == "u":
            latest_update = self.client_latest_update[client_name]
            if latest_update < len(self.game_state_list) - 1:
                print(client_name + "'s OLD state: " + str(latest_update))
                answer = self.game_state_list[latest_update:]
                for c in answer:
                    # print(c)
                    pass
                self.client_latest_update[client_name] = len(self.game_state_list) -1 # sets the new index
            else:
                answer = "0"
        # Client sent a ClickPacket
        elif type == "1" or type == "2" or type == "3":
            click_packet = clickpacket.ClickPacket()
            click_packet.deserialize(client_message)
            self.game_state_list.append(click_packet)   # Update game state
            self.game_state_sender.append(client_name)  # Update game state sender
            # self.print_game_state_list()
            answer = None                               # Do not send back an answer
        # Client sent a request to join a game
        elif type == "j":
            self.client_latest_update[client_name] = -1
            self.print_clients()
            # self.print_game_state_list()
            answer = newgamepacket.NewGamePacket(board=self.board).serialize()
        # Client sent an erroneous message
        else:
            answer = "Jag har tagit emot ditt meddelande, men förstod inte vad du sa"

        return answer

    async def main(self):
        server = await asyncio.start_server(self.handle_client, self.address, self.port)

        address = server.sockets[0].getsockname()
        # print(f'Serving on {address}')

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    # Prepares the string commands that were sent in to the correct format for the main function
    i = sys.argv[1:]
    # print(i)
    # print(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5]), bool(i[6]))
    game_server = GameServer(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5]), bool(i[6]))
    asyncio.run(game_server.main())
