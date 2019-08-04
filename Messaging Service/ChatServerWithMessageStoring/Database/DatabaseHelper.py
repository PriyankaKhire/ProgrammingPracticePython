#Database helper functions
import os
import shelve

class DatabaseHelper(object):
    
    def writeToHash(self, fileName, key, value):
        hashFile_object = shelve.open(fileName)
        hashFile_object[key] = value
        hashFile_object.close()

    def getAllValues(self, fileName):
        hashFile_object = shelve.open(fileName)
        values = []
        for key in hashFile_object:
            values.append(hashFile_object[key])
        hashFile_object.close()
        return values

    def getValue(self, fileName, key):
        if not(self.isKeyInHash(fileName, key)):
            return False
        hashFile_object = shelve.open(fileName)
        value = hashFile_object[key]
        hashFile_object.close()
        return value
        
    def isKeyInHash(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        if (key in hashFile_object):
            value = hashFile_object[key]
            hashFile_object.close()
            return True
        return False
