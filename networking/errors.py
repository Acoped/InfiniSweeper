"""Custom exceptions for the networking package"""


class Error(Exception):
    pass


class ClickPacketDeserializeError(Error):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
