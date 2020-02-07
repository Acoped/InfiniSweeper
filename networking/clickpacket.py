from networking.errors import *


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
        try:
            split = message.split("_")
            try:
                if all(isinstance(int(item), int) for item in split):
                    self.action = split[0]
                    self.x = split[1]
                    self.y = split[2]
            except ValueError:
                raise ClickPacketDeserializeError("Badly formatted string '" + message + "' could not be deserialized",
                                                  "At least one value separated by '_' is not integer")
        except IndexError:
            raise ClickPacketDeserializeError("Badly formatted string '" + message + "' could not be deserialized",
                                              "Too few '_' delimiters")


# ----- Testing ----- (mbe write unit tests?)

# Sending
send_packet = ClickPacket(1, 356, 123)
print(send_packet)
print(send_packet.serialize())

# Receiving
received_packet = ClickPacket()
received_packet.deserialize("2_531_83")
print(received_packet)
