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
    def deserialize(self, message : str):
        my_list = message.split("_")
        self.action = my_list[0]
        self.x = my_list[1]
        self.y = my_list[2]
        """
        try:
        except:
            print("Faulty string, could not deserialize to ClickPacket")"""

send_packet = ClickPacket(1, 356, 123)
print(send_packet)
print(send_packet.serialize())

recv_packet = ClickPacket()
recv_packet.deserialize("2_531_987")
print(recv_packet)
