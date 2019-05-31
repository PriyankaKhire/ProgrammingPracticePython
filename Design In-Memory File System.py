#Design In-Memory File System
# https://leetcode.com/problems/design-in-memory-file-system/
class File(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content
        
class Directory(object):
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []
        
class FileSystem(object):
    def __init__(self):
        self.root = self.createDirectory("/")
        self.lastVisitedDirectory = None

    def createDirectory(self, name):
        return Directory(name)

    def createFile(self, name, content):
        return File(name, content)

    def dirExists(self, sourceDir, dirName):
        for dirObject in sourceDir.directories:
            if(dirObject.name == dirName):
                return True
        return False

    def fileExists(self, sourceDir, fileName):
        for fileObject in sourceDir.files:
            if(fileObject.name == fileName):
                return True
        return False

    def findDirectory(self, sourceDir, dirName):
        for dirObject in sourceDir.directories:
            if(dirObject.name == dirName):
                return dirObject
        return False

    def findFile(self, sourceDir, fileName):
        for fileObject in sourceDir.files:
            if(fileObject.name == fileName):
                return fileObject
        return False

    #def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        

    def mkdir(self, path):
        if(len(path) == 1 and path == "/"):
            return
        dirs = path.split("/")
        sourceDir = self.root
        for d in dirs:
            if(d != ''):
                if not(self.dirExists(sourceDir, d)):
                    print "Created directory ", d, " in ", sourceDir.name
                    directory = self.createDirectory(d)
                    sourceDir.directories.append(directory)
                else:
                    print "Directory ", d, " already exists in dir ", sourceDir.name
                    directory = self.findDirectory(sourceDir, d)
                sourceDir = directory
        self.lastVisitedDirectory = sourceDir
        """
        :type path: str
        :rtype: None
        """
        

    def addContentToFile(self, filePath, content):
        self.mkdir(filePath[:-2])
        fileName = filePath.split("/")[-1]
        #get the last directory and find if file with that name exists or not.
        if not(self.fileExists(self.lastVisitedDirectory, fileName)):
            print "Created a file ", fileName, " in directory ",self.lastVisitedDirectory.name
            fileObject = self.createFile(fileName, content)
            self.lastVisitedDirectory.files.append(fileObject)
        else:
            #append content
            print "File ", fileName, " already exists so we appended content to it"
            fileObject = self.findFile(self.lastVisitedDirectory, fileName)
            fileObject.content = fileObject.content + content
            print "New file content is ", fileObject.content            
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        

    #def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

#Main
obj = FileSystem()
obj.mkdir("/a/b/c")
obj.mkdir("/a/b/c/d/e")
obj.addContentToFile("/a/b/c/d/e/f", "Hello World")
obj.addContentToFile("/a/b/c/d/e/f", " How are you ?")
