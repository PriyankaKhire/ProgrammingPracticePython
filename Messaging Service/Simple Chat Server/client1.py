import socket, threading
sys.path.append("../")
from Config import PortConfig

class Client(object):
    def __init__(self):
        self.serverName = 'SimpleChatServer'
        pc = PortConfig()
        port = pc.port[self.serverName]

def getMessage(s):
    while True:
        s.send(raw_input("Message: "))
    
#Main

s = socket.socket()
s.connect((host, port))

background_thread = threading.Thread(target=getMessage, args=(s,))
background_thread.daemon = True
background_thread.start()

while True:
    print s.recv(1024), "\n"


