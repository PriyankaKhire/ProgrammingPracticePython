#Client
import sys
sys.path.append("../../../HelperFunctions")
from Client import Client
sys.path.append("../../../../ASCII Images")
from AsciiImages import AsciiImages

class FeatureBasedShardingClient(object):
    def __init__(self):
        self.name = 'FeatureBasedPartitioningClient'
        self.img = AsciiImages()

    def sendData(self, name, data):
        client = Client(name)
        client.putData(data)

    def run(self):
        user_name = raw_input("Enter the user name : ")
        email = raw_input("Enter email address : ")
        tweet = raw_input("Please enter your tweet : ")
        print "\nChose one of the following images"
        for imgName in self.img.images:
            print imgName
        imageName = raw_input("\nType the full name of the image: ")
        self.sendData('FeatureBasedPartitioningServer', user_name)
        self.sendData('FeatureBasedPartitioningServer', email)
        self.sendData('FeatureBasedPartitioningServer', tweet)
        self.sendData('FeatureBasedPartitioningServer', self.img.images[imageName])

#Main
obj = FeatureBasedShardingClient()
obj.run()
