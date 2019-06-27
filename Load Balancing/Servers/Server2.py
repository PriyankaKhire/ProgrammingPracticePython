import socket
import sys
sys.path.append("..")
from Config import ServerConfig

class Server(object):
    def __init__(self):
        self.name = "Server2"
        sc = ServerConfig()
        self.s = socket.socket()
        self.port = sc.port[self.name]
        self.s.bind(('', self.port))
        self.s.listen(5)

    def startServer(self):
        connection, address = self.s.accept()
        print connection.recv(1024)
        connection.send('Connected to '+self.name)
        connection.close()

    def run(self):
        print self.name+" started...\n"
        while True:
            self.startServer()

#Main
obj = Server()
obj.run()
