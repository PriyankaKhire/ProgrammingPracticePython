#Database
import os
import socket, pickle
import sys
from HelperFunctions import HelperFunctions
sys.path.append("../Server")
from PasteClass import Paste

class Database(object):
    def __init__(self):
        self.port = 1009
        self.hashFile = "index.txt"
        self.hs = HelperFunctions()

    def server(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(5)
        print "Started server"
        return s
    
    def logic(self, pasteObj, key):
        #The given key already exists 
        if(self.hs.isKeyInHash(self.hashFile, key)):
            return False
        #Write the text to file and put in folder
        self.hs.createFolder(pasteObj.folderName+"_"+pasteObj.userId)
        self.hs.createFile(os.path.join(pasteObj.folderName+"_"+pasteObj.userId, pasteObj.fileName), pasteObj.text)
        #insert in hash key = key, value = path of text file
        self.hs.writeToHash(self.hashFile, key, os.path.join(pasteObj.folderName+"_"+pasteObj.userId, pasteObj.fileName))
        print "File created"
        return True
        
    def run(self):
        #Start the server
        s = self.server()
        while True:
            connection, addr = s.accept()
            pasteObj_string = connection.recv(4096)
            pasteObj = pickle.loads(pasteObj_string)
            connection.send('Database server has recieved the paste object successfully')
            key = connection.recv(1024)
            connection.send('Database server has recieved the key')
            if(self.logic(pasteObj, key)):
                connection.send("True")
            else:
                connection.send("False")
            connection.close()

#Main
obj = Database()
obj.run()
