#Database
import os
import shelve

class HelperFunctions(object):

    def ifFile(self,fileName):
        if not os.path.isfile(fileName):
            #print "File does not exist"
            return False
        return True

    def isEmpty(self, fileName):
        file_object = open(fileName, "r")
        for line in file_object:
            if(line.strip() != ""):
                file_object.close()
                return False
        file_object.close()
        return True

    def write(self, fileName, string):
        file_object = open(fileName, "a")
        file_object.write(string+"\n")
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
    
    def createFolder(self, folderName):
        if not os.path.exists(folderName):
            os.makedirs(folderName)

    def createFile(self, fileName, text):
        f = open(fileName+".txt", "w")
        f.write(text)
        f.close()

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
        return False

    def isKeyInHash(self, fileName, key):
        hashFile_object = shelve.open(fileName)
        if (key in hashFile_object):
            value = hashFile_object[key]
            hashFile_object.close()
            return True
        return False
