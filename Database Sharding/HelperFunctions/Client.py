import socket
from Config import PortConfig

#Name indicates the name of the server the client wants to connect to
class Client(object):
    def __init__(self, name):
        self.s = socket.socket()
        pc = PortConfig()
        self.port = pc.port[name]

    def putData(self, data):
        self.s.connect(('127.0.0.1', self.port))
        self.s.send(data)
        self.s.close()

    def getData(self, byteSize):
        self.s.connect(('127.0.0.1', self.port))
        data = self.s.recv(byteSize)
        self.s.close()
        return data
