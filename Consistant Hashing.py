#Consistant Hashing
#https://www.youtube.com/watch?v=tHEyzVbl4bg
class Server(object):
    def __init__(self, serverID):
        self.id = serverID
        self.name = "Server "+str(serverID)
        self.cache = []

class HashFunctions(object):
    def explanation(self):
        print "Remember our hash functions need to be consistant and should always output same value for same request ID"

    def requestHashFunction(self, requestID):
        return requestID+253

    #obviously these are not some good hash funcitons. But for demo this is ok.
    def serverHashFunction1(self, serverID):
        return serverID*10+25

    def serverHashFunction2(self, serverID):
        return serverID*10+50

    def serverHashFunction3(self, serverID):
        return serverID*10+75
        
class ConsistantHashing(object):
    def __init__(self):
        self.servers = []
        self.hashFunctions = HashFunctions()
        #let's have an id space that is circular
        self.idSpaceSize = 100
        #obviously we can't represent this in any data structure so we take an array
        self.idSpace = [None for i in range(self.idSpaceSize)]
        #to begin with we only start with one server
        self.addServer()

    #this is to help you visualise how the circular space id would look 
    def printIDSpace(self):
        space = 0
        for i in range((self.idSpaceSize/4)+1):
            n1 = i
            n2 = self.idSpaceSize-i-1
            subctract_Space1 = 0
            subctract_Space2 = 0
            if(self.idSpace[n1]):
                n1 = self.idSpace[n1].name
                subctract_Space1 = 4
                subctract_Space2 = 5
            if(self.idSpace[n2]):
                n2 = self.idSpace[n2].name
                subctract_Space2 = 4
            print ((self.idSpaceSize/2)-i-subctract_Space1)*" ", n1, (space-subctract_Space2)*" ", n2
            space = space+2
        space = space-4
        for i in range(self.idSpaceSize/4 + 1, self.idSpaceSize/2):
            n1 = i
            n2 = self.idSpaceSize-i-1
            subctract_Space1 = 0
            subctract_Space2 = 0
            if(self.idSpace[n1]):
                n1 = self.idSpace[n1].name
                subctract_Space1 = 4
                subctract_Space2 = 5
            if(self.idSpace[n2]):
                n2 = self.idSpace[n2].name
                subctract_Space2 = 4
            print (i+1-subctract_Space1)*" ", n1, (space-subctract_Space2)*" ", n2
            space = space-2

    def mapToIDSpace(self, hashID):
        return hashID%self.idSpaceSize

    def addVirtualServers(self, server):
        #since the server exists on more than one spot in the id space we call these virtual servers.
        print "Here our server ", server.id, " is virtually added to id space ",
        hashID2 = self.hashFunctions.serverHashFunction2(server.id)
        mappedID2 = self.mapToIDSpace(hashID2)
        self.idSpace[mappedID2] = server
        print mappedID2
        #clean out cache of next server, because we be stealing requests now.
        self.dumpNextServerCache(server, mappedID2+1)
        hashID3 = self.hashFunctions.serverHashFunction3(server.id)
        mappedID3 = self.mapToIDSpace(hashID3)
        self.idSpace[mappedID3] = server
        print "The next space we have added our virtual server to is ", mappedID3
        #clean out cache.
        self.dumpNextServerCache(server, mappedID3+1)
        print "The id space now looks like "
        self.printIDSpace()

    def mapServersToIDSpace(self, server):
        #Take the recently added server
        #put the server id through hash funcitons
        #and map it to id space
        print "Adding server ", server.id," to id space ",
        hashID = self.hashFunctions.serverHashFunction1(server.id)
        mappedID = self.mapToIDSpace(hashID)
        self.idSpace[mappedID] = server
        print mappedID
        #dump the server's cache that's to the clock wise of our newly added server.
        self.dumpNextServerCache(server, mappedID+1)
        print "Now what if we add or remove servers ? the request load would be unevenly distributed"
        print "To tackle this issue we map 1 server to more than one id space and call it a virtual server"
        self.addVirtualServers(server)

    def dumpNextServerCache(self, server, mappedID):
        if(len(self.servers) == 1):
            return
        #Our newly added server is now going to steal requests from its immediate next server in ID space.
        next_server = None
        while not(self.idSpace[mappedID]):
            mappedID = (mappedID+1)%self.idSpaceSize
        print "Dumping the cache of server ", self.idSpace[mappedID].id, " mapped to id space ", mappedID
        self.idSpace[mappedID].cache = []
                

    def addServer(self):
        #create new server
        new_server = Server(len(self.servers))
        self.servers.append(new_server)
        self.mapServersToIDSpace(new_server)

    def assignRequestToServer(self, requestID, cacheInfo):
        print "Assigning this request to server ",
        while not(self.idSpace[requestID]):
            requestID = (requestID+1)%self.idSpaceSize
        print self.idSpace[requestID].id
        #update server side cache
        if not(cacheInfo in self.idSpace[requestID].cache):
            self.idSpace[requestID].cache.append(cacheInfo)
        print "The server holds cache ", self.idSpace[requestID].cache                                                                                                                                                         

    def logic(self):
        print "To begin with we only have 1 server"
        choice = "y"
        while (choice == "y"):
            requestID = input("Please enter request ID ")
            #get the hash id for given request
            hashID = self.hashFunctions.requestHashFunction(requestID)
            #map this hash id to the id space
            hashIDMappedToIDSpace = self.mapToIDSpace(hashID)
            print "Request ID ", requestID, " mapped to id space ", hashIDMappedToIDSpace
            #Assign it to the server.
            self.assignRequestToServer(hashIDMappedToIDSpace, "Request ID: "+str(requestID))
            choice = raw_input("Would you like to continue ? Y/N ").lower()
            changeInServer = raw_input("Would you like to add a server ? Y/N ").lower()
            if(changeInServer == 'y'):
                self.addServer()
    
#Main
obj = ConsistantHashing()
obj.logic()
