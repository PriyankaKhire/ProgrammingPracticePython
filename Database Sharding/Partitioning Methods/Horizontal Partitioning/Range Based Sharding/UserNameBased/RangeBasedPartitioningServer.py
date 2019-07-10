#Server
import sys
import os, os.path
sys.path.append("../../../../HelperFunctions")
from Server import Server
from Client import Client

class Explanation(object):
    
    def explanation1(self):
        print "In this approch we try to store data by letter of the alphabet, the user name begins with"

    def con1(self):
        print "\n What happens if we want to add or remove server ?"
        print "With the approch above there would be way too many redirects"
        print "We take help of consistant hashing to reduce the number of redirects"

    def con2(self):
        print "What happens if there are way too many users with username that begins with letter A as compared to users that have username starting with letter X"
        print "One shard will have too much data and others wont"

    def pro1(self):
        print "While finding data, what if we want to find data across shards ?"
        print "With this approch, since all data of one user lies on same shard, it would be easy"

class RangeBasedShardingServer(object):
    def __init__(self):
        self.name = 'RangeBasedPartitioningServer'
        self.server = Server(self.name)
        self.exp = Explanation()

    def sendData(self, name, data):
        client = Client(name)
        client.putData(data)

    def getNumberOfShardingServers(self):
        return len(os.listdir('../../../../Shards'))

    def logic(self, data):
        print "We first get number of sharding servers"
        numberOfShards = self.getNumberOfShardingServers()
        print "We then get the first letter of the user name, since we get the data in format <userName> : <data>"
        print "We can just get the user name from data[0]"
        firstLetter = data[0]
        letterIndex = ord(firstLetter.lower()) - ord('a')
        print "Since the first letter of the user name is ", firstLetter
        shardNumber = letterIndex%numberOfShards
        print "We store this data on Shard ", shardNumber+1
        self.exp.con1()
        self.sendData('Master'+str(shardNumber+1), data)        

    def run(self):
        self.exp.explanation1()
        while True:
            print self.name + ' ready to get data'
            data = self.server.getData(1024)
            print 'Got data ', data
            self.logic(data.strip())

#Main
obj = RangeBasedShardingServer()
obj.run()

