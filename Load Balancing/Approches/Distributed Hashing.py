#Distributed Hashing
import os, os.path
import socket
import sys
sys.path.append("..")
from Config import ApprochConfig, ServerConfig

class Explanation(object):
    
    def explanation1(self):
        print "The client generates a request Id between 0 to M"

    def explanation2(self):
        print "We take this request Id and then mod it with number of servers"
        print "and then return the port number"

    def cons(self):
        print "https://www.toptal.com/big-data/consistent-hashing"
        

class Server(object):
    def __init__(self):
        self.name = "Approch1"
        self.exp = Explanation()
        ac = ApprochConfig()
        self.s = socket.socket()
        self.port = ac.port[self.name]
        self.s.bind(('', self.port))
        self.s.listen(5)

    def getNumberOfServers(self):
        return len(os.listdir('../Servers'))

    def logic(self, requestId):
        print "Total number of servers is ",self.getNumberOfServers()
        self.exp.explanation2()
        #server number is generated from 0 to numberOfServers-1, but our server numbers start from 1 to N
        serverNumber = requestId%self.getNumberOfServers()
        sc = ServerConfig()
        #so we add one to even that out.
        return sc.port['Server'+str(serverNumber+1)]

    def startServer(self):        
        connection, address = self.s.accept()
        self.exp.explanation1()
        requestId = connection.recv(1024)
        print "Recieved request Id ", requestId
        serverPort = self.logic(int(requestId))
        print "Sending server port number ",serverPort
        connection.send(str(serverPort))
        connection.close()

    def run(self):
        print self.name+" server started...\n"
        while True:
            self.startServer()

#Main
obj = Server()
obj.run()
