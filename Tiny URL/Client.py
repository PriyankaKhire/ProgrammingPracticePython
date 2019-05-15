#Tiny URL Client
import socket
import sys
sys.path.append("..")
from ColorText import ColorText
import random

class Client(object):
    def __init__(self):
        self.id = random.randint(1, 300)
        self.longURL = None
        self.s = socket.socket()

    def displayPage(self):
        ct = ColorText()
        ct.display(4*"\t"+"Tiny URL", "red-highlight")

    def run(self):
        #self.displayPage()
        self.longURL = raw_input("Enter a long URL to make tiny:\n")
        #To connect to port of server
        port = 7
        self.s.connect(('127.0.0.1', port))
        self.s.send(self.longURL)
        self.s.close()

#Main
obj = Client()
obj.run()
        
        
