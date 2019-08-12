#Database helper functions
import os
import shelve

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

    def getAllValues(self, fileName):
        hashFile_object = shelve.open(fileName)
        values = []
        for key in hashFile_object:
            values.append(hashFile_object[key])
        hashFile_object.close()
        return values
