import socket
import threading

def getMessage(s):
    while True:
        s.send(raw_input("Message: "))
    
#Main
port = 1043
host = 'localhost'
s = socket.socket()
s.connect((host, port))

background_thread = threading.Thread(target=getMessage, args=(s,))
background_thread.daemon = True
background_thread.start()

while True:
    print s.recv(1024), "\n"


