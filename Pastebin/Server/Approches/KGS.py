#Key Generating System
import socket
import sys
import random, string
sys.path.append("../../Database")
from HelperFunctions import HelperFunctions

class Explanation(object):

    def explanation1(self):
        print "We first start by generating unique keys, that are not present in usedKeysDB"
        print "Then we check if unUsed keys db is empty, or if not created at all"
        print "If either of these 2 conditions are true then we generate 10 keys and put them in the database"
        
    def explanation2(self):
        print "Then we check cache, if cache is empty we take 5 keys from unUsed keys database and load them in cache"
        print "After loading them in cache we move those loaded keys to usedKeys database"

    def cons(self):
        print "Aint KGS single point of faliure ?"
        print "yes, to tackle this issue, we can have another standby KGS"

class KGS(object):
    def __init__(self):
        self.exp = Explanation()
        self.hf = HelperFunctions()
        self.port = 21
        self.usedKeysDB = "../../Database/usedKeysDB.txt"
        self.keyDatabase = "../../Database/unUsedKeyDB.txt"
        self.cache = []

    def getKey(self):
        key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
        return key

    def generateNKeys(self, n):
        keys = []
        for i in range(n):
            key = self.getKey()
            #while keys in used keys database, generate new key.
            while(self.hf.isKeyInHash(self.usedKeysDB, key)):
                key = self.getKey()
            keys.append(key)
        return keys

    def writeKeysToFile(self, keys, fileName):
        keyString = ""
        for key in keys:
            keyString = keyString + key + "\n"
        self.hf.write(fileName, keyString)

    def fillKeyDatabase(self):
        self.exp.explanation1()
        #if the file doesnt exits then create it and fill it with generated keys
        # or if file is empty then fill it with keys
        if((not self.hf.ifFile(self.keyDatabase))  or (self.hf.isEmpty(self.keyDatabase))):
            keys = self.generateNKeys(10)
            self.writeKeysToFile(keys, self.keyDatabase)
            return

    def loadKeysInCache(self):
        self.exp.explanation2()
        #if the keys database is empty or missing first create that
        self.fillKeyDatabase()
        #Get 5 keys from database 
        for i in range(5):
            key = self.hf.getKey(self.keyDatabase)[:-1]
            #load the key in cache
            self.cache.append(key)
            #put the key in used database
            self.hf.writeToHash(self.usedKeysDB, key, "True")
        print self.cache

    #test function.
    def checkIfKeysInCacheAreInUsedKeysDB(self):
        for key in self.cache:
            if(self.hf.readFromHash(self.usedKeysDB, key) != "True"):
                return False
        return True

    def refreshCache(self):
        if not self.cache:
            self.loadKeysInCache()

    def server(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(5)
        print "Started server"
        return s

    def run(self):
        #Start the server
        s = self.server()
        while True:
            connection, addr = s.accept()
            self.refreshCache()
            connection.send(self.cache.pop())
            connection.close()
        

#Main
obj = KGS()
obj.run()
    
