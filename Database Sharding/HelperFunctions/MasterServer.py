#Master
import sys
import os.path
from Server import Server
from Client import Client
from Database import Database

class MasterServer(object):
    def __init__(self, name):
        self.name = name
        self.folderName = 'Data'
        self.server = Server(self.name)
        self.db = Database()

    def sendDataToSlave(self, slaveName, data):
        client = Client(slaveName)
        client.putData(data)

    def write(self, data):
        self.db.createFolder(self.folderName)
        self.db.write(os.path.join(self.folderName, self.name+'.txt'), data)

    def run(self, slaveList):
        while True:
            print self.name + ' Server ready to get data'
            data = self.server.getData(1024)
            print 'Got data ', data
            self.write(data)
            for slave in slaveList:
                self.sendDataToSlave(slave, data)
                print "Sent data to ", slave
            print "\n"
        
