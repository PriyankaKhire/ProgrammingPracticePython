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
        if(dirName == ''):
            return sourceDir
        for dirObject in sourceDir.directories:
            if(dirObject.name == dirName):
                return dirObject
        return False

    def findFile(self, sourceDir, fileName):
        for fileObject in sourceDir.files:
            if(fileObject.name == fileName):
                return fileObject
        return False

    def ifFilePath(self, path):
        potentialFileName = path.split("/")[-1]
        sourceDir = self.root
        for directory in path.split("/")[:-1]:
            if(directory != ''):
                sourceDir = self.findDirectory(sourceDir, directory)
        self.lastVisitedDirectory = sourceDir
        fileObject = self.findFile(sourceDir, potentialFileName)
        if(fileObject != False):
            return True
        return False
                
                    

    def ls(self, path):
        if(self.ifFilePath(path)):
            return [path.split("/")[-1]]
        #get directory object
        dirObj =  self.findDirectory(self.lastVisitedDirectory, path.split("/")[-1])
        dirContents = []
        for fileObj in dirObj.files:
            dirContents.append(fileObj.name)
        for dObj in dirObj.directories:
            dirContents.append(dObj.name)
        dirContents.sort()
        return dirContents        
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
        self.mkdir('/'.join(filePath.split('/')[:-1]))
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
        

    def readContentFromFile(self, filePath):
        sourceDir = self.root
        for directory in filePath.split("/")[:-1]:
            if(directory != ''):
                sourceDir = self.findDirectory(sourceDir, directory)
        fileObj = self.findFile(sourceDir, filePath.split("/")[-1])
        return fileObj.content
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
print obj.mkdir("/a/b/c")
print obj.mkdir("/a/b/c/d/e")
print obj.addContentToFile("/a/b/c/d/e/f", "Hello World")
print obj.addContentToFile("/a/b/c/d/e/f", " How are you ?")
print obj.mkdir("/a/b/c/d/e/g/h")
print obj.addContentToFile("/a/b/c/d/e/i", "Hello World")
print obj.ls("/a/b/c/d/e")
print obj.readContentFromFile("/a/b/c/d/e/f")

obj2 = FileSystem()
print obj2.ls("/")
print obj2.mkdir('/a/b/c')
print obj2.addContentToFile('/a/b/c/d', 'hello')
print obj2.ls("/")
print obj2.readContentFromFile('/a/b/c/d')


obj3 = FileSystem()
obj3.mkdir("/zijzllb")
print obj3.ls('/')
print obj3.ls('/zijzllb')
obj3.mkdir('r')
print obj3.ls('/')
print obj3.ls('/r')
obj3.addContentToFile("/zijzllb/hfktg","d")
print obj3.readContentFromFile('/zijzllb/hfktg')
print obj3.ls('/')
print obj3.readContentFromFile("/zijzllb/hfktg")
