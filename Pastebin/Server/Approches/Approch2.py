#Approch 1
import socket,  pickle
import sys
import random, string
sys.path.append("..")
from PasteClass import Paste

class Explanation(object):

    def explanation1(self):
        print "In this approch we get key from KGS and store in database"
        
class Approch2(object):
    def __init__(self):
        self.exp = Explanation()
        self.port = 2

    def server(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(5)
        print "Started server"
        return s

    def getKey(self):
        kgsPort = 21
        s = socket.socket()
        s.connect(('127.0.0.1', kgsPort))
        key = s.recv(1024)
        s.close()
        return key

    def logic(self, pasteObj):
        self.exp.explanation1()
        key = self.getKey()
        print "Got key ",key," from KGS"
        #Send it to database
        port = 1009
        s = socket.socket()
        s.connect(('127.0.0.1', port))
        object_string = pickle.dumps(pasteObj)
        s.send(object_string)
        print s.recv(1024)
        s.send(key)
        print s.recv(1024)
        if(s.recv(1024) == "True"):
            print "File created successfully"
        else:
            print "File not created"
        s.close()  

    def run(self):
        #Start the server
        s = self.server()
        flag = True
        while flag:
            connection, addr = s.accept()
            pasteObj_string = connection.recv(4096)
            pasteObj = pickle.loads(pasteObj_string)
            connection.send('Approch 2 server has recieved the paste object successfully')
            connection.close()
            self.logic(pasteObj)
            flag = False

#Main
obj = Approch2()
obj.run()

