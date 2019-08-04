#User Conversation Class for database
class UserConversation(object):
    def __init__(self):
        self.userName = None
        #For this hash the key is the other userName and value is the message queue.
        self.conversationHistory = {}
        self.unreadMessages = {}
