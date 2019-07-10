#Slave
import sys
import os.path
from Server import Server
from Database import Database

class SlaveServer(object):
    def __init__(self, name, masterName):
        self.name = name
        self.master = masterName
        self.folderName = 'Data'
        self.server = Server(self.name)
        self.db = Database()
        #if server doesn't have updated copy of Master data then copy the data.
        self.copyMasterData()
        
    def copyMasterData(self):
        #we have the master data
        if (self.db.ifFile(os.path.join(self.folderName, self.name+'.txt'))):
            return
        #if master data doesnt exist
        if not(self.db.ifFile(os.path.join(self.folderName, self.master+'.txt'))):
            return
        masterData = self.db.read(os.path.join(self.folderName, self.master+'.txt'))
        self.db.write(os.path.join(self.folderName, self.name+'.txt'), masterData)

    def write(self, data):
        self.db.createFolder(self.folderName)
        self.db.write(os.path.join(self.folderName, self.name+'.txt'), data)

    def run(self):
        while True:
            print self.name+ ' Server ready to get data'
            data = self.server.getData(1024)
            print 'Got data ', data
            self.write(data)
            print "\n"
        
        
