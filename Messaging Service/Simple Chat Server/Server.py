import socket, sys
from thread import *
sys.path.append("../")
from Config import PortConfig

class Server(object):
    def __init__(self):
        self.name = 'SimpleChatServer'
        pc = PortConfig()
        port = pc.port[self.name]
        server = socket.socket()
        server.bind((self.name, port))
        server.listen(5)
        self.clients = []

    def ClientThread(connection):
        while True:
            message = connection.recv(1024)
            connection.send("Ack\n")
            Broadcast(connection, message)

    def Broadcast(connection, message):
        for conn in self.clients:
            if(conn != connection):
                conn.send(message)

    def AcceptConnections():
        while True:
            connection, address = s.accept()
            print "Got connection from ",connection
            self.clients.append(connection)
            start_new_thread(ClientThread, (connection, clients))

    def run():
        self.AcceptConnections()

#Main
obj = Server()
obj.run()


