#Pastebin Client
import socket
import sys
sys.path.append("..")
from ColorText import ColorText

class Client(object):
    def __init__(self):
        self.userId = None
        self.s = socket.socket()
        self.text = ""
        self.fileName = "DefaultFileName"
        #Not giving user this option currently
        self.expiryDate = '1 minute'
        self.folderName = "DefaultFolderName"
        self.sizeLimitInBytes = 1024
        self.port = 8

    def displayPage(self):
        ct = ColorText()
        ct.display(4*"\t"+"Pastebin", "red-highlight")

    def getStringSizeInBytes(self, string):
        return len(string.encode('utf-8'))

    def checkSize(self, string):
        stringSize = self.getStringSizeInBytes(string)
        if(int(stringSize) > self.sizeLimitInBytes):
            return False
        return True

    def getText(self):
        self.text = raw_input("Enter text (limit 1024 bytes): \n")
        while(not self.checkSize(self.text)):
            print "Text size too large"
            self.text = raw_input("Enter text (limit 1024 bytes): \n")
            
    def getFileName(self):
        choice = raw_input("Would you like to enter FILE name (y/n): ")
        if(choice.lower() != 'y'):
            return
        self.fileName = raw_input("Enter file name: ")
        while(not self.checkSize(self.fileName)):
            print "Text size too large"
            self.fileName = raw_input("Enter file name: ")

    def getFolderName(self):
        choice = raw_input("Would you like to enter FOLDER name (y/n): ")
        if(choice.lower() != 'y'):
            return
        self.folderName = raw_input("Enter folder name: ")
        while(not self.checkSize(self.folderName)):
            print "Text size too large"
            self.folderName = raw_input("Enter folder name: ")

    def getUserId(self):
        self.userId = raw_input("Enter User Id: ")

    def run(self):
        self.displayPage()
        self.getUserId()
        self.getText()
        self.getFileName()
        self.getFolderName()
        #To connect to port of server
        self.s.connect(('127.0.0.1', self.port))
        self.s.send(self.userId)
        print self.s.recv(self.sizeLimitInBytes)
        self.s.send(self.text)
        print self.s.recv(self.sizeLimitInBytes)
        self.s.send(self.fileName)
        print self.s.recv(self.sizeLimitInBytes)
        self.s.send(self.folderName)
        print self.s.recv(self.sizeLimitInBytes)
        self.s.close()

#Main
obj = Client()
obj.run()
