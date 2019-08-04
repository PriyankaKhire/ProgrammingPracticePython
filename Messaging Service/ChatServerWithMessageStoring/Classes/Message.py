class Message(object):
    def __init__(self):
        self.message = None
        #sender and receiver are just user names and not user objects
        self.sender = None
        self.receiver = None
        self.timeStamp = None
        self.sequenceNumber = None
