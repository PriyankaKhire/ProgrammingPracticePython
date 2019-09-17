#Database helper functions
import os, shelve 

class DatabaseHelper(object):
    
    def writeToHash(self, fileName, key, value):
        try:
            hashFile_object = shelve.open(fileName)
            hashFile_object[key] = value
            hashFile_object.close()
        except:
            print "Please try accessing the file",fileName,"again"

    def isKeyInHash(self, fileName, key):
        try:
            hashFile_object = shelve.open(fileName)
            if (key in hashFile_object):
                hashFile_object.close()
                return True
            return False
        except:
            print "Please try accessing the file",fileName,"again"

    def getValue(self, fileName, key):
        if not(os.path.isfile(fileName)):
            return None
        try:
            hashFile_object = shelve.open(fileName)
            value = hashFile_object[key]
            hashFile_object.close()
            return value
        except:
            print "Please try accessing the file",fileName,"again"
    

    def getAllValues(self, fileName):
        if not(os.path.isfile(fileName)):
            return []
        try:
            hashFile_object = shelve.open(fileName)
            values = [hashFile_object[key] for key in hashFile_object]
            hashFile_object.close()
            return values
        except:
            print "Please try accessing the file",fileName,"again"

    def getAllKeys(self, fileName):
        if not(os.path.isfile(fileName)):
            return []
        try:
            hashFile_object = shelve.open(fileName)
            keys = [key for key in hashFile_object]
            hashFile_object.close()
            return keys
        except:
            print "Please try accessing the file",fileName,"again"
