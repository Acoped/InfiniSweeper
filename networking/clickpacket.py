class ClickPacket:
    """
    A class representing game state change (clicking) data to be sent or received for a multi-player game over a network
    """

    def __init__(self, action: int = None, x: int = None, y: int = None):
        self.action = action    # 1 for left click, 2 for right click, 3 for double click
        self.x = x              # x coordinate of the clicked tile
        self.y = y              # y coordinate of the clicked tile

    def __str__(self):
        return 'ClickPacket object ' \
               '[action = ' + str(self.action) + ', x = ' + str(self.x) + ', y = ' + str(self.y) + ']'

    def serialize(self) -> str:
        return str(self.action) + '_' + str(self.x) + '_' + str(self.y)

    def deserialize(self, message: str):
        split = message.split("_")
        self.action = split[0]
        self.x = split[1]
        self.y = split[2]


def test():
    # ----- Testing ----- (mbe write unit tests?)

    # Sending
    send_packet = ClickPacket(1, 356, 123)
    print(send_packet)

    # Receiving
    received_message = send_packet.serialize()
    print(received_message)
    received_packet = ClickPacket()
    received_packet.deserialize(received_message)
    print(received_packet)

if __name__ == '__main__':
    pass
    test()