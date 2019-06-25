#Database
import os
import socket, pickle
import sys
import shelve
sys.path.append("../Server")
from PasteClass import Paste

class Database(object):
    def __init__(self):
        self.port = 1007
        self.hashFile = "index.txt"

    def server(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(5)
        print "Started server"
        return s
    
    def createFolder(self, folderName):
        if not os.path.exists(folderName):
            os.makedirs(folderName)

    def createFile(self, fileName, text):
        f = open(fileName+".txt", "w")
        f.write(text)
        f.close()

    def writeToHash(self, fileName, key, value):
        hashFile_object = shelve.open(fileName)
        hashFile_object[key] = value
        hashFile_object.close()

    def readFromHash(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        if (key in hashFile_object):
            value = hashFile_object[key]
            hashFile_object.close()
            return value
        return False

    def isKeyInHash(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        if (key in hashFile_object):
            value = hashFile_object[key]
            hashFile_object.close()
            return True
        return False

    def logic(self, pasteObj, key):
        #The given key already exists 
        if(self.isKeyInHash(self.hashFile, key)):
            return False
        #Write the text to file and put in folder
        self.createFolder(pasteObj.folderName+"_"+pasteObj.userId)
        self.createFile(os.path.join(pasteObj.folderName+"_"+pasteObj.userId, pasteObj.fileName), pasteObj.text)
        #insert in hash key = key, value = path of text file
        self.writeToHash(self.hashFile, key, os.path.join(pasteObj.folderName+"_"+pasteObj.userId, pasteObj.fileName))
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
            connection.close()
            if(self.logic(pasteObj, key)):
                connection.send(True)
            else:
                connection.send(False)

#Main
obj = Database()
obj.run()
