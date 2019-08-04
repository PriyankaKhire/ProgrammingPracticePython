import socket, sys, pickle, time, datetime
from thread import *
sys.path.append("../Classes")
from Message import Message
sys.path.append("../../")
from Config import PortConfig

class Server(object):
    def __init__(self):
        self.name = 'MessageStoreChatServer'
        self.pc = PortConfig()
        port = self.pc.port[self.name]
        self.server = socket.socket()
        self.server.bind(('localhost', port))
        self.server.listen(5)
        self.clients = {}

    def getFromDatabase(self, sender, receiver, connection):
        print "Getting conversation history for ", sender, " from ", receiver
        serverName = 'GetMessagesDatabase'
        port = self.pc.port[serverName]
        server = socket.socket()
        server.connect(('localhost', port))
        server.send(sender)
        print server.recv(1024),
        server.send(receiver)
        print server.recv(1024)
        #recv top 10 recent messages
        recentMessage = server.recv(5000)
        while(recentMessage!="Done"):
            connection.send(recentMessage)
            # Receive a message from database and sent to client
            time.sleep(0.5)
            recentMessage = server.recv(5000)
        server.close()

    def storeInDatabase(self, message, delivaryStatus):
        print "Going to store "+ delivaryStatus +" message in database "
        serverName = 'StoreMessagesDatabase'
        port = self.pc.port[serverName]
        server = socket.socket()
        server.connect(('localhost', port))
        server.send(message)
        print server.recv(1024)
        server.send(delivaryStatus)
        print server.recv(1024)
        server.close()

    def ping(self, connection):
        connection.send("ping")
        if(connection.recv(1024)=="ping"):
            return True

    def createMessage(self, message):
        m = Message()
        m.message = message
        m.sender = self.name
        m.timeStamp = datetime.datetime.fromtimestamp(time.time())
        m_str = pickle.dumps(m)
        return m_str

    def removeConnectionFromHash(self, connection):
        for client in self.clients:
            if(self.clients[client] == connection):
                print "Removing the client ", client
                del self.clients[client]
                print self.clients
                return

    def ClientThread(self, connection, newlyOpenedConnection, sender, receiver):
        try:
            while (self.ping(connection)):
                #For the first time, get the conversation history of this sender
                if(newlyOpenedConnection == True):
                    self.getFromDatabase(sender, receiver, connection)
                    newlyOpenedConnection = False
                message = connection.recv(3072)
                connection.send("Ack")
                self.sendMessage(connection, message)                
        except Exception as e:
            print "\nClosing the conneciton with ", connection
            print "Exception: ", e
            connection.close()
            #Remove client from clients hash
            self.removeConnectionFromHash(connection)

    def deliverMessage(self, connection, message):
        connection.send(message)

    def sendMessage(self, connection, message):
        message_obj = pickle.loads(message)
        reciever = message_obj.receiver
        if not(reciever in self.clients):
            m = self.createMessage(reciever+" is not online")
            self.deliverMessage(connection, m)
            self.storeInDatabase(message, 'unread')
            return
        self.deliverMessage(self.clients[reciever], message)
        self.storeInDatabase(message, 'read')

    def AcceptConnections(self):
        while True:
            connection, address = self.server.accept()
            clientName = connection.recv(1024)
            connection.send("Establisehd connection with server")
            recieverName = connection.recv(1024)
            print "Connected to sender ",clientName, " and receiver ", recieverName
            self.clients[clientName] = connection
            start_new_thread(self.ClientThread, (connection, True, clientName, recieverName))

    def run(self):
        print "Server Started"
        self.AcceptConnections()

#Main
obj = Server()
obj.run()
