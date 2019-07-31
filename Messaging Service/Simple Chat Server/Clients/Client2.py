import socket, threading, sys, pickle, os, time, datetime
sys.path.append("../")
from Message import Message
sys.path.append("../../")
from Config import PortConfig

class Client(object):
    def __init__(self):
        self.name = os.path.basename(__file__)[:-3]
        self.reciever = self.getFriend()
        self.serverName = 'SimpleChatServer'
        pc = PortConfig()
        port = pc.port[self.serverName]
        self.server = socket.socket()
        self.server.connect(('localhost', port))
        #Send server your name so server can save it in a hash along with your conneciton id
        self.server.send(self.name)

    def getFriend(self):
        available_clients = self.getListOfAvailableClients()
        index_number = input("Enter the index number of the client you'd like to send message to " + str(available_clients)+" ")
        while(index_number < 0 or index_number > len(available_clients)-1):
            index_number = input("Index number out of range, please enter a different number ")
        return available_clients[index_number]

    def getListOfAvailableClients(self):
        #get all client file names
        client_files = os.listdir(os.getcwd())
        # remove .py from the file name
        all_clients = [client.split(".")[0] for client in client_files]
        # get the name of all clients that are not you
        clients = [client for client in all_clients if client!=self.name]
        return clients

    def putMessage(self):
        sequenceNumber = 0
        while True:
            message = Message()
            message.message = raw_input()
            message.sender = self.name
            message.receiver = self.reciever
            message.timeStamp = datetime.datetime.fromtimestamp(time.time())
            message.sequenceNumber = sequenceNumber
            message_string = pickle.dumps(message)
            self.server.send(message_string)
            sequenceNumber = sequenceNumber+1

    def processMessage(self, message):
        if(message == "ping"):
                self.server.send("ping")
        elif(message == "Ack"):
            return
        elif(message == "Delivered"):
            print "Delivered"
        else:
            message_obj = pickle.loads(message)
            print message_obj.sender, " at ",message_obj.timeStamp
            print message_obj.message, "\n"

    def getMessage(self):
        while True:
            message = self.server.recv(1024)
            self.processMessage(message)

    def run(self):
        print "Started ", self.name
        background_thread = threading.Thread(target=self.putMessage)
        background_thread.daemon = True
        background_thread.start()
        self.getMessage()
    
#Main
obj = Client()
obj.run()
