#Client sending objects
import socket, pickle
import socket, pickle
from SampleClass import SampleClass

HOST = 'localhost'
PORT = 10
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Create an instance of SampleClass() to send to server.
obj = SampleClass()
# Pickle the object and send it to the server
obj_string = pickle.dumps(obj)
s.send(obj_string)

s.close()
print 'Data Sent to Server'
