#Key Generation Service
import sys
import os,binascii
import socket  
sys.path.append("../../..")
from ColorText import ColorText
sys.path.append("../../DataBase")
from DataBase import DataBase
class Explanation(object):
    
    def explanation1(self):
        print "So in this approch we first start with generating unique 8 character keys offline and store it in database"

    def explanation2(self):
        print "When ever we need a key we first look into cache if it has kesy then we give the client that key"
        print "Else we take some pregenerated keys from database and bring them in cache"

    def explanation3(self):
        print "As soon as the keys are brought into cache we mark them as used in database"
        print "This ensures that each server gets unique keys"

    def explanation4(self):
        print "This system needs to make sure that it doesn't hand out same key to different servers"
        print "For this it needs to have a proper lock over internal database"

class EncodeURL(object):
    def __init__(self):
        self.ct = ColorText()
        self.exp = Explanation()
        self.db = DataBase()
        self.unUsedKeys = "../../DataBase/unUsedKeys.txt"
        self.usedKeys = "../../DataBase/usedKeys.txt"
        self.cachedKeys = []
        self.s = socket.socket()

    def generateKeysWriteToDB(self):
        keys = ""
        for i in range(10):
            keys = keys + str(binascii.b2a_hex(os.urandom(4)))+"\n"
        self.db.write(self.unUsedKeys, keys)

    def bringKeysToCache(self):
        self.exp.explanation3()
        for i in range(5):
            key = self.db.getKey(self.unUsedKeys)[:-1]
            self.cachedKeys.append(key)
            self.db.writeToHash(self.usedKeys, key, "True")
        print self.cachedKeys

    def returnKey(self):
        if not (self.db.ifFile(self.unUsedKeys)):
            self.exp.explanation1()
            self.generateKeysWriteToDB()
        if not self.cachedKeys:
            self.exp.explanation2()
            self.bringKeysToCache()
        self.exp.explanation4()
        return self.cachedKeys.pop()

    def server(self):
        port = 5
        self.s.bind(('', port))
        self.s.listen(5)
        print "Started server"

    def run(self):
        self.ct.display(4*"\t"+"Approch2", "black-highlight")
        #Start the server
        self.server()
        while True:
            key = self.returnKey()
            #Send key to client
            c, addr = self.s.accept()
            c.send(key)
            print "Sent key ",key, " to client ", addr
            c.close()
        
#Main
obj = EncodeURL()
obj.run()
