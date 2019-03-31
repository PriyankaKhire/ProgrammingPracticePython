#Simple Load Balancer
#https://www.youtube.com/watch?v=K0Ta65OqQkY
import random
class Server(object):
    def __init__(self):
        self.cache = []
        
class HashingLoadBalancer(object):
    def __init__(self):
        self.servers = [Server()]

    def explanation(self):
        print "This load balancer takes number of servers at given point and a request ID"
        print "And maps the request to specific server"

    #very poorly written hash function.
    def hashFunction(self, requestID):
        return requestID%10

    def assignToServer(self, hashNumber, requestNumber):
        infoAboutRequestID = "requestID "+str(requestNumber)
        serverNumber = hashNumber%len(self.servers)
        server = self.servers[serverNumber]
        #add info about request to server cache
        if not (infoAboutRequestID in server.cache):
            server.cache.append(infoAboutRequestID)
        return serverNumber

    def addServer(self):
        self.servers.append(Server())

    def logic(self):
        print "To begin with we only have 1 server"
        choice = "y"
        while (choice == "y"):
            requestID = input("Please enter request ID ")
            hashNumber = self.hashFunction(requestID)
            serverNumber = self.assignToServer(hashNumber, requestID)
            print "The current request is now being server by server number ", serverNumber
            print "Server number ", serverNumber, "'s cache currently holds this info ", self.servers[serverNumber].cache
            choice = raw_input("Would you like to continue ? Y/N ").lower()
            changeInServer = raw_input("Would you like to add a server ? Y/N ").lower()
            if(changeInServer == 'y'):
                self.addServer()
        print "This demos how when you add a server the cache info becomes outdated"
            

#Main
obj = HashingLoadBalancer()
obj.logic()
