import os.path

class Database(object):

    def read(self, fileName):
        output = ""
        if not self.ifFile(fileName):
            return output
        file_object = open(fileName, "r")
        for line in file_object:
            output = output + line
        file_object.close()
        return output

    def ifFile(self,fileName):
        if not os.path.isfile(fileName):
            #print "File does not exist"
            return False
        return True
    
    def write(self, fileName, string):
        file_object = open(fileName, "a")
        file_object.write(string+"\n")
        file_object.close()

    def createFolder(self, folderName):
        if not os.path.exists(folderName):
            os.makedirs(folderName)
