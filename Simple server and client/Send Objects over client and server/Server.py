#Server reciving objects
import socket, pickle
from SampleClass import SampleClass

#Create a connectionection
HOST = 'localhost'
PORT = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print "Server started"
connection, addr = s.accept()
print 'Connected by', addr
#recieve the object string
object_string = connection.recv(4096)
obj = pickle.loads(object_string)
connection.close()
print 'Data received from client'
print obj, obj.string, obj.intiger
