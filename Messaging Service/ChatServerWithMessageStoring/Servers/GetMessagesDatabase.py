#Database server that gets unread messages and conversation history of user.
import sys, socket, pickle, time, threading
from thread import *
sys.path.append("../Classes")
from UserConversation import UserConversation
sys.path.append("../Database")
from DatabaseHelper import DatabaseHelper
sys.path.append("../../")
from Config import PortConfig
class GetMessagesDatabase(object):
    def __init__(self):
        self.name = 'GetMessagesDatabase'
        self.convoFile = '../Database/ConversationHistory'
        self.pc = PortConfig()
        port = self.pc.port[self.name]
        self.server = socket.socket()
        self.server.bind(('localhost', port))
        self.server.listen(5)

    def getConversaitonHistoryObject(self, userName):
        conversationHistory = DatabaseHelper().getValue(self.convoFile, userName)
        if(conversationHistory == False):
            print "There is no conversation history between these users"
            return
        return conversationHistory

    def appendUnreadConvoToReadConvo(self,conversationHistoryObj, receiver):
        if(receiver in conversationHistoryObj.unreadMessages):
            conversationHistoryObj.conversationHistory[receiver] = conversationHistoryObj.conversationHistory[receiver] + conversationHistoryObj.unreadMessages[receiver]
            del conversationHistoryObj.unreadMessages[receiver]
            #store the modified ch object in database
            DatabaseHelper().writeToHash(self.convoFile, conversationHistoryObj.userName, conversationHistoryObj)
        #Return the most recent 10 convos from the q
        return conversationHistoryObj.conversationHistory[receiver][-10:]
        
    def getConvoHistory(self, sender, receiver):
        #The logic here is to first check if this sender has any unread messages from this receiver
        #all we do is take the messages out from unread messages queue and
        #append the unread messages with read messages and then return top 10 messages
        #this avoids any complexities of just showing unread messages, and we are sending reasonable ammount of messages
        #if the sender wishes to read more messages they can send the request of last read convo and we and send 10 more messages.
        print "The sender is ", sender
        print "The receiver is ", receiver
        #Get the conversation history of the sender
        senderChObj = self.getConversaitonHistoryObject(sender)
        if(senderChObj != None):
            return self.appendUnreadConvoToReadConvo(senderChObj, receiver)
        return None

    def sendRecentMessages(self, connection, sender, receiver):
        #Get and then send the convo history
        recentMessages = self.getConvoHistory(sender, receiver)
        if(recentMessages == None):
            connection.send("Done")
            return
        #Send the messages
        for message in recentMessages:
            connection.send(pickle.dumps(message))
            #this delay to ensure no packets get lost.
            #to prevent this delay i would send one large compressed packet in real world.
            time.sleep(1.5)
        connection.send("Done")

    def AcceptConnections(self):
        while True:
            connection, address = self.server.accept()
            sender = connection.recv(1024)
            connection.send("Fetching conversation history of the sender")
            receiver = connection.recv(1024)
            connection.send("from the receiver")
            start_new_thread(self.sendRecentMessages, (connection, sender, receiver))

    def run(self):
        print "Database server to get messages started"
        self.AcceptConnections()

#Main
obj = GetMessagesDatabase()
obj.run()
