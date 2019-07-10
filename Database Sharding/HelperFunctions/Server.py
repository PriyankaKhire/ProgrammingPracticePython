import socket
from Config import PortConfig

class Server(object):
    def __init__(self, name):
        pc = PortConfig()
        port = pc.port[name]
        self.s = socket.socket()
        self.s.bind(('', port))
        self.s.listen(5)

    def putData(self, data):
        client, address = self.s.accept()
        client.send(data)
        client.close()

    def getData(self, byteSize):
        client, address = self.s.accept()
        data = client.recv(byteSize)
        client.close()
        return data 
