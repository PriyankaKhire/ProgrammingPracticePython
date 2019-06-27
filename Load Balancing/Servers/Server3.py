import socket
import sys
sys.path.append("..")
from Config import ServerConfig
sys.path.append("../Database")
from Database import Database

class Server(object):
    def __init__(self):
        self.name = "Server3"
        sc = ServerConfig()
        self.db = Database()
        self.s = socket.socket()
        self.port = sc.port[self.name]
        self.s.bind(('', self.port))
        self.s.listen(5)

    def saveData(self, data):
        serverFile = '../Database/'+self.name+'.txt'
        if (self.db.isKeyInHash(serverFile, data)):
            print 'Data '+data+' already in '+self.name+' database'
            return
        print 'Data '+data+' not in '+self.name+' database'
        print 'Saving data...\n\n'
        self.db.writeToHash(serverFile, data, 'True')
                            
        
    def startServer(self):
        connection, address = self.s.accept()
        print connection.recv(1024)
        connection.send('Connected to '+self.name)
        data = connection.recv(1024)
        print "Got data ", data
        connection.close()
        self.saveData(data)

    def run(self):
        print self.name+" started...\n"
        while True:
            self.startServer()

#Main
obj = Server()
obj.run()
