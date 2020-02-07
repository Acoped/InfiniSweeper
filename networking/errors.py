class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ClickPacketDeserializeError(Error):
    """Error that should be thrown when click packet cannot deserialize"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message