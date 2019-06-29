#Consistent Hashing
import os, os.path
import socket
import sys
from ConsistentHashingMainFunctionality import MainFunctionality
sys.path.append("..")
from Config import ApprochConfig, ServerConfig, ClientData

class Explanation(object):
    
    def explanation1(self):
        print "Here we try to solve the drawback of distributed hashing"
        print "We need a distribution scheme that does not depend directly on the number of servers, "
        print "so that, when adding or removing servers, the number of keys that need to be relocated is minimized."
        
        

class Server(object):
    def __init__(self):
        self.name = "Approch2"
        self.exp = Explanation()
        ac = ApprochConfig()
        self.s = socket.socket()
        self.port = ac.port[self.name]
        self.s.bind(('', self.port))
        self.s.listen(5)
        self.cd = ClientData()
        self.requestMap = {}
        self.requestHash = {}

    def putInRequestMap(self, requestId, serverNumber):
        clientData = self.cd.data[requestId]
        if(requestId in self.requestMap):          
            print "Previously the data", clientData, "was in Server", self.requestMap[requestId]
        print "The data ", clientData, " is now being placed in Server", serverNumber
        self.requestMap[requestId] = serverNumber

    def getServerNumber(self, requestId):
        mf = MainFunctionality()
        serverNumber, self.requestHash = mf.logic(requestId, self.requestHash)
        return serverNumber

    def logic(self, requestId):
        serverNumber = self.getServerNumber(requestId)
        sc = ServerConfig()
        #Update the request map
        self.putInRequestMap(requestId, serverNumber+1)
        #so we add one to even that out.
        return sc.port['Server'+str(serverNumber+1)]

    def startServer(self):        
        connection, address = self.s.accept()
        requestId = connection.recv(1024)
        print "Recieved request Id ", requestId
        serverPort = self.logic(int(requestId))
        print "Sending server port number ",serverPort
        connection.send(str(serverPort))
        connection.close()

    def run(self):
        self.exp.explanation1()
        print self.name+" server started...\n"
        while True:
            self.startServer()
            print "\n"

#Main
obj = Server()
obj.run()
