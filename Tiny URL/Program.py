#Main Program
from Client import Client
class MainProgram(object):
    def __init__(self):
        self.client = Client()

    def runClient(self):
        self.client.run()
        print self.client.longURL, self.client.id
        
#Main
obj = MainProgram()
obj.runClient()
