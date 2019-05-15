#Server
import socket
import sys
from Helper import Helper
sys.path.append("../DataBase")
from DataBase import DataBase
class Server(object):
    def __init__(self):
        self.id = 1
        self.helper = Helper()
        self.db = DataBase()
        self.usedKeys = "../DataBase/usedKeys.txt"

    def getKey(self):
        s = socket.socket()
        #To contact port of approch 2
        port = 5
        s.connect(('127.0.0.1', port))
        key = s.recv(1024)
        s.close()
        return key

    def storeKey(self, url):
        #Shorten the url
        url = self.helper.removeCommonPrefixes(url)
        #get key for the URL
        key = self.getKey()
        print "Got key ", key
        #Store it in DataBase
        self.db.writeToHash(self.usedKeys, key, url)
        #Verify if key stored successfully in database
        if(self.db.readFromHash(self.usedKeys, key) == url):
            print "Key stored successfully in database"
            return True
        return False

    def server(self):
        s = socket.socket()
        port = 7
        s.bind(('', port))
        s.listen(5)
        print "Started server"
        return s

    def run(self):
        #Start the server
        s = self.server()
        while True:
            c, addr = s.accept()
            url = c.recv(1024)
            if not(self.storeKey(url)):
                print "Some Error occoured while storing in database"
            c.close()

        
#Main
obj = Server()
obj.run()
