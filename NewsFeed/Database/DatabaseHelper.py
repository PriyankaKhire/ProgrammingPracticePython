#Database helper functions
import os, shelve 

class DatabaseHelper(object):
    
    def writeToHash(self, fileName, key, value):
        hashFile_object = shelve.open(fileName)
        hashFile_object[key] = value
        hashFile_object.close()

    def isKeyInHash(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        if (key in hashFile_object):
            value = hashFile_object[key]
            hashFile_object.close()
            return True
        return False

    def getValue(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        value = hashFile_object[key]
        hashFile_object.close()
        return value

    def getAllValues(self, fileName):
        if not(os.path.isfile(fileName)):
            return []
        hashFile_object = shelve.open(fileName)
        values = [hashFile_object[key] for key in hashFile_object]
        hashFile_object.close()
        return values

    def getAllKeys(self, fileName):
        if not(os.path.isfile(fileName)):
            return []
        hashFile_object = shelve.open(fileName)
        keys = [key for key in hashFile_object]
        hashFile_object.close()
        return keys
