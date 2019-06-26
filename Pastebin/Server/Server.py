#Server
import socket, pickle
import sys
from PasteClass import Paste
class Server(object):
    def __init__(self):
        self.id = 1
        self.port = 8

    def server(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(5)
        print "Started server"
        return s

    def sendToApproches(self, pasteObj, port):
        s = socket.socket()
        s.connect(('127.0.0.1', port))
        object_string = pickle.dumps(pasteObj)
        s.send(object_string)
        print s.recv(1024)
        s.close()

    def approch1(self, pasteObj):
        #Send data to Approch1 server
        self.sendToApproches(pasteObj, 1)
        

    def approch2(self, pasteObj):
        #Send data to Approch2 server
        self.sendToApproches(pasteObj, 2)

    def processData(self, text, fileName, folderName, userId):
        #We first create Paste object.
        pasteObj = Paste(userId, text, fileName, folderName)
        self.approch1(pasteObj)
        self.approch2(pasteObj)
        

    def run(self):
        #Start the server
        s = self.server()
        while True:
            c, addr = s.accept()
            userId = c.recv(1024)
            c.send('Server acknowledges receipt of user id')
            text = c.recv(1024)
            c.send('Server acknowledges receipt of text')
            print "Got text from user ", userId, " the text is \n ", text
            fileName = c.recv(1024)
            c.send('Server acknowledges receipt of file name')
            folderName = c.recv(1024)
            c.send('Server acknowledges receipt of folder name')
            print "File Name ", fileName, " Folder Name ", folderName
            c.close()
            self.processData(text, fileName, folderName, userId)

#Main
obj = Server()
obj.run()
