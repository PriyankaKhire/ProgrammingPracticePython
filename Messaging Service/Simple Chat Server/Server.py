import socket, sys, pickle, time, datetime
from thread import *
from Message import Message
sys.path.append("../")
from Config import PortConfig

class Server(object):
    def __init__(self):
        self.name = 'SimpleChatServer'
        pc = PortConfig()
        port = pc.port[self.name]
        self.server = socket.socket()
        self.server.bind(('localhost', port))
        self.server.listen(5)
        self.clients = {}

    def ping(self, connection):
        connection.send("ping")
        if(connection.recv(1024)=="ping"):
            return True

    def createMessage(self, message):
        m = Message()
        m.message = message
        m.sender = self.name
        m.timeStamp = datetime.datetime.fromtimestamp(time.time())
        return m

    def removeConnectionFromHash(self, connection):
        for client in self.clients:
            if(self.clients[client] == connection):
                print "Removing the client ", client
                del self.clients[client]
                print self.clients
                return

    def ClientThread(self, connection):
        try:
            while (self.ping(connection)):               
                message = connection.recv(2048)
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
            return
        self.deliverMessage(self.clients[reciever], message)

    def AcceptConnections(self):
        while True:
            connection, address = self.server.accept()
            clientName = connection.recv(1024)
            print "Connected to ",clientName, " with connection id ", connection
            self.clients[clientName] = connection
            start_new_thread(self.ClientThread, (connection,))

    def run(self):
        print "Server Started"
        self.AcceptConnections()

#Main
obj = Server()
obj.run()


