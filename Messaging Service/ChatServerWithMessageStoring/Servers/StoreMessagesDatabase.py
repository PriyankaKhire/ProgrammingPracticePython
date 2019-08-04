#Database server to store messages to database.
import socket, sys, pickle
sys.path.append("../Classes")
from Message import Message
from UserConversation import UserConversation
sys.path.append("../Database")
from DatabaseHelper import DatabaseHelper
sys.path.append("../../")
from Config import PortConfig

class StoreMessagesDatabase(object):
    def __init__(self):
        self.name = 'StoreMessagesDatabase'
        self.convoFile = '../Database/ConversationHistory'
        self.pc = PortConfig()
        port = self.pc.port[self.name]
        self.server = socket.socket()
        self.server.bind(('localhost', port))
        self.server.listen(5)

    def getConversaitonHistoryObject(self, userName):
        conversationHistory = DatabaseHelper().getValue(self.convoFile, userName)
        if(conversationHistory == False):
            #Create new conversation history object
            conversationHistory = UserConversation()
            conversationHistory.userName = userName
        return conversationHistory

    def storeMessageInReadConvoHistory(self, chObj, message, otherUser):
        print "Storing messages in read convo history"
        if not(otherUser in chObj.conversationHistory):
            chObj.conversationHistory[otherUser] = [message]
        else:
            chObj.conversationHistory[otherUser].append(message)

    def storeMessageInUnReadConvoHistory(self, chObj, message, otherUser):
        print "Storing messages in unread convo history"
        if not(otherUser in chObj.unreadMessages):
            chObj.unreadMessages[otherUser] = [message]
        else:
            chObj.unreadMessages[otherUser].append(message)

    def writeConvoHistoryObjToDB(self, userName, chObj):
        print "Writing convos to db"
        DatabaseHelper().writeToHash(self.convoFile, userName, chObj)

    def processMessage(self, message, recieverDelivaryStatus):
        #Here we first get the user conversation history object from the conversation history database
        #in reality this database would be stored on database shards, and there is probably more logic involved
        #in storing the data, but since this is a small project and database sharding was covered saparately previously
        #we are just storing the data all in one file.   
        messageObj = pickle.loads(message)
        print "Sender ", messageObj.sender
        print "Reciever ", messageObj.receiver
        print "Reciever delivary status ", recieverDelivaryStatus
        #Get the sender conversation history object
        senderChObj = self.getConversaitonHistoryObject(messageObj.sender)
        print senderChObj
        #since the sender would have read the message they sent, we put it in their read convohistory
        print "Sender messages ",
        self.storeMessageInReadConvoHistory(senderChObj, messageObj, messageObj.receiver)
        #Write convo history object to database
        self.writeConvoHistoryObjToDB(messageObj.sender, senderChObj)
        #Get the receiver conversation history object
        receiverChObj = self.getConversaitonHistoryObject(messageObj.receiver)
        print receiverChObj
        print "Receiver messages ",
        if(recieverDelivaryStatus == 'unread'):
            self.storeMessageInUnReadConvoHistory(receiverChObj, messageObj, messageObj.sender)
        else:
            self.storeMessageInReadConvoHistory(receiverChObj, messageObj, messageObj.sender)
        #Write convo history object to database
        self.writeConvoHistoryObjToDB(messageObj.receiver, receiverChObj)

    def AcceptConnections(self):
        while True:
            connection, address = self.server.accept()
            message = connection.recv(3072)
            connection.send("Database got message")
            recieverDelivaryStatus = connection.recv(1024)
            connection.send("Storing message in database")
            self.processMessage(message, recieverDelivaryStatus)
            connection.close()

    def run(self):
        print "Database server started"
        self.AcceptConnections()

#Main
obj = StoreMessagesDatabase()
obj.run()
