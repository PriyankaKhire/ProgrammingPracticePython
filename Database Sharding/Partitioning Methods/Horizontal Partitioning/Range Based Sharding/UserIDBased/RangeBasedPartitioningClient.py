#Client
import sys
sys.path.append("../../../../HelperFunctions")
from Client import Client

class RangeBasedShardingClient(object):
    def __init__(self):
        self.name = 'RangeBasedPartitioningClient'

    def sendData(self, name, data):
        client = Client(name)
        client.putData(data)

    def run(self):
        user_id = raw_input("What is the user id : ")
        data = raw_input("Please enter data : ")
        self.sendData('RangeBasedPartitioningServer', user_id+" : "+data)

#Main
obj = RangeBasedShardingClient()
obj.run()
