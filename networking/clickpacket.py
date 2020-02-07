from networking.errors import *

class ClickPacket():
    """
    A class representing clicking data to be sent or received for a multiplayer game over a network
    """

    # Use this constructor for sending a game state change, a click
    def __init__(self, action : int = None, x : int = None, y : int = None):
        self.action = action    # 1 for left click, 2 for right click, 3 for double click
        self.x = x              # x coordinate of the clicked tile
        self.y = y              # y coordinate of the clicked tile

    # Method for nice printout of the object when using print function
    def __str__(self):
        return 'ClickPacket object [action = ' + str(self.action) + ', x = ' + str(self.x) + ', y = ' + str(self.y) + ']'

    # Serializes object to a string that can be sent
    def serialize(self) -> str:
        return str(self.action) + '_' + str(self.x) + '_' + str(self.y)

    # Deserializes a correctly formated string to the ClickPacket instance, otherwise throws a ClickPacketDeserializeError
    # In the client receiving, Maybe check for ClickPackets first, and if it throws an error, check instead for NewGamePackets?
    def deserialize(self, message : str):
        try:
            list = message.split("_")
            try:
                if all(isinstance(int(item), int) for item in list):
                    self.action = list[0]
                    self.x = list[1]
                    self.y = list[2]
            except ValueError:
                raise ClickPacketDeserializeError("Badly formated string '" + message + "' could not be deserialized", "At least one value seperated by '_' is not integer")
        except IndexError:
            raise ClickPacketDeserializeError("Badly formated string '" + message + "' could not be deserialized", "Too few '_' delimiters")


send_packet = ClickPacket(1, 356, 123)
print(send_packet)
print(send_packet.serialize())

recv_packet = ClickPacket()
recv_packet.deserialize("2_531_83")
print(recv_packet)
