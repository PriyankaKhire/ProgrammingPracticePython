#Key Generation Service
import sys
import os.path
import os,binascii
import shelve
sys.path.append("../../..")
from ColorText import ColorText
class Explanation(object):
    
    def explanation1(self):
        print "So in this approch we first start with generating unique 8 character keys offline and store it in database"

    def explanation2(self):
        print "When ever we need a key we first look into cache if it has kesy then we give the client that key"
        print "Else we take some pregenerated keys from database and bring them in cache"

    def explanation3(self):
        print "As soon as the keys are brought into cache we mark them as used in database"
        print "This ensures that each server gets unique keys"

    def explanation4(self):
        print "This system needs to make sure that it doesn't hand out same key to different servers"
        print "For this it needs to have a proper lock over internal database"


class DataBase(object):

    def isEmpty(self, fileName):
        file_object = open(fileName, "r")
        for line in file_object:
            if(line.strip() != ""):
                file_object.close()
                return False
        file_object.close()
        return True

    def ifFile(self,fileName):
        if not os.path.isfile(fileName):
            #print "File does not exist"
            return False
        return True

    def write(self, fileName, string):
        file_object = open(fileName, "a")
        file_object.write(string+"\n")
        file_object.close()

    def read(self, fileName):
        if not self.ifFile(fileName):
            return
        file_object = open(fileName, "r")
        for line in file_object:
            print line,
        file_object.close()

    def getKey(self, fileName):
        if not self.ifFile(fileName):
            return
        file_object = open(fileName, 'r')
        lines = file_object.readlines()
        file_object.close()
        i = 0
        while(lines[i].strip() == ""):
            i = i+1
        key = lines[i]
        file_object = open(fileName, 'w')
        file_object.write(''.join(lines[i+1:]))
        file_object.close()
        #if file empty then delete it
        if(self.isEmpty(fileName)):
            os.remove(fileName)
        return key

    def writeToHash(self, fileName, key, value):
        hashFile_object = shelve.open(fileName)
        hashFile_object[key] = value
        hashFile_object.close()

    def readFromHash(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        if (key in hashFile_object):
            value = hashFile_object[key]
        hashFile_object.close()
        return value

class EncodeURL(object):
    def __init__(self):
        self.ct = ColorText()
        self.exp = Explanation()
        self.db = DataBase()
        self.unUsedKeys = "unUsedKeys.txt"
        self.usedKeys = "usedKeys.txt"
        self.cachedKeys = []

    def generateKeysWriteToDB(self):
        keys = ""
        for i in range(10):
            keys = keys + str(binascii.b2a_hex(os.urandom(4)))+"\n"
        self.db.write(self.unUsedKeys, keys)

    def bringKeysToCache(self):
        self.exp.explanation3()
        for i in range(5):
            key = self.db.getKey(self.unUsedKeys)[:-1]
            self.cachedKeys.append(key)
            self.db.writeToHash(self.usedKeys, key, "True")
        print self.cachedKeys

    def run(self, string):
        self.ct.display(4*"\t"+"Approch2", "black-highlight")
        self.exp.explanation1()
        if not (self.db.ifFile(self.unUsedKeys)):
            self.generateKeysWriteToDB()
        self.exp.explanation2()
        if not self.cachedKeys:
            self.bringKeysToCache()
        self.exp.explanation4()
        return self.cachedKeys.pop()
        
        
        

#Main
obj = EncodeURL()
obj.run("google.com")
