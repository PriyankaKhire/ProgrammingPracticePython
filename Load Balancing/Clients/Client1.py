from random import randint
import socket                
import sys
sys.path.append("..")
from Config import ApprochConfig

class Client(object):
    def __init__(self):
        self.name = 'Client1'
        self.approchPort = ApprochConfig()  

    def requestId(self):
        return(randint(0, 1000))

    def connectToApprochServer(self, approchPort):
        s = socket.socket()
        requestIdNumber = self.requestId()
        print "Generated request id ", requestIdNumber
        s.connect(('127.0.0.1', approchPort))
        #send request ID
        s.send(str(requestIdNumber))
        serverPort = s.recv(1024)
        print "Got server port ", serverPort
        s.close()
        return int(serverPort)

    def approch1(self):
        approchPort = self.approchPort.port['Approch1']
        return self.connectToApprochServer(approchPort)

    def choseServer(self):
        return self.approch1()

    def run(self):
        s = socket.socket()
        serverPort = int(self.choseServer())
        s.connect(('127.0.0.1', serverPort))
        s.send("Getting data from "+self.name)
        print s.recv(1024)
        s.close()  

#Main
obj = Client()
obj.run()
