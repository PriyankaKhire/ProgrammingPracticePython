#Approch 1
import socket,  pickle
import sys
import random, string
sys.path.append("..")
from PasteClass import Paste

class Explanation(object):

    def mainExplanaiton(self):
        print "In this approch we generate randome key and try to store data against that key in hash table"
        print "If the key generated already exist in database then we generate another key"
    
    def explanation1(self):
        print "Just like tiny url here also we generate 7 character long alphanumeric key"
        print "This key can contain A-Z, a-z and 0-9"

class Approch1(object):
    def __init__(self):
        self.exp = Explanation()
        self.port = 1

    def server(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(5)
        print "Started server"
        return s
    
    def generateKey(self):
        self.exp.explanation1()
        key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
        return key

    def logic(self, pasteObj):
        self.exp.mainExplanaiton()
        key = self.generateKey()
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
            print "Successfully created and stored the text file in database"
        else:
            print "The key already exists in database, retrying..."
            self.logic(pasteObj)
        s.close()
        

    def run(self):
        #Start the server
        s = self.server()
        while True:
            connection, addr = s.accept()
            pasteObj_string = connection.recv(4096)
            pasteObj = pickle.loads(pasteObj_string)
            connection.send('Approch 1 server has recieved the paste object successfully')
            connection.close()
            self.logic(pasteObj)
        

#Main
obj = Approch1()
obj.run()
