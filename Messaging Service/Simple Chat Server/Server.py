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

    def ClientThread(self, connection):
        try:
            while (self.ping(connection)):               
                message = connection.recv(2048)
                connection.send("Ack")
                self.sendMessage(connection, message)                
        except Exception as e:
            print "\nClosing the conneciton with ", connection
            print e
            connection.close()

    def messageDelivary(self, connection):
        if(connection.recv(1024) == "Ack"):
            print "Successfully delivered message to ", connection
            return True
        return False

    def sendMessage(self, connection, message):
        message_obj = pickle.loads(message)
        reciever = message_obj.receiver
        if not(reciever in self.clients):
            m = self.createMessage(reciever+" is not online")
            connection.send(pickle.dumps(m))
            self.messageDelivary(connection)
            return
        self.clients[reciever].send(message)
        if(self.messageDelivary(self.clients[reciever])):
            delivered = self.createMessage("Message delivered to "+reciever)
            connection.send(pickle.dumps(delivered))

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


