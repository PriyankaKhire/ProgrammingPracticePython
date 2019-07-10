#Server
import sys
import os, os.path
sys.path.append("../../../HelperFunctions")
from Server import Server
from Client import Client

class Explanation(object):
    
    def explanation1(self):
        print "Here we assign each shard for each feature"
        
    def con1(self):
        print "But as you saw, images are larger than other data"
        print "So the shard holding images will be heavier than other shards"

    def con2(self):
        print "Finding all data about one user may take time since we have to go through different shards"

class FeatureBasedShardingServer(object):
    def __init__(self):
        self.name = 'FeatureBasedPartitioningServer'
        self.server = Server(self.name)
        self.exp = Explanation()

    def sendData(self, name, data):
        client = Client(name)
        client.putData(data)

    def logic(self, user_name, email, tweet, image):
        print "We have assigned each shard for one feature"
        print "Here user name is the key on every shard"
        print "We store user name and email on shard 1"
        self.sendData('Master1', user_name+" : "+email)
        print "We store user name and tweet on shard 2"
        self.sendData('Master2', user_name+" : "+tweet)
        print "We store user name and image on shard 3"
        self.sendData('Master3', user_name+" : \n"+image+"\n")

    def run(self):
        self.exp.explanation1()
        while True:
            print self.name + ' ready to get data'
            user_name = self.server.getData(1024)
            print 'User Name: ', user_name
            email = self.server.getData(1024)
            print 'Email Address: ', email
            tweet = self.server.getData(1024)
            print 'Tweet: ', tweet
            image = self.server.getData(1024)
            print 'Image: \n', image
            self.logic(user_name, email, tweet, image)

#Main
obj = FeatureBasedShardingServer()
obj.run()

