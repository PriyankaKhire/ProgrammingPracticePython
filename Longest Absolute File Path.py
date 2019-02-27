#Longest Absolute File Path
#https://leetcode.com/problems/longest-absolute-file-path/

#the logic is to form a complete N-ary tree, while adding childern we always add from left to right
class TreeNode(object):
    def __init__(self, name, fileType):
        self.name = name
        self.childern = []
        self.fileType = fileType

class Tree(object):
    def __init__(self):
        self.root = None
        self.longestFilePath = ""

    def createNode(self, name, fileType):
        node = TreeNode(name, fileType)
        return node

    def addChild(self, node, child):
        node.childern.append(child)
        return

    def dfs(self, node, output):
        if not(node.childern):
            if('.' in node.name):
                if(len(self.longestFilePath) < len(output)):
                    self.longestFilePath = output
            return
        for child in node.childern:
            self.dfs(child, output+"\\"+child.name)

    def dfsTraversal(self):
        self.dfs(self.root, self.root.name)
        
class Solution(object):
    def __init__(self):
        self.trees = []
        self.longestFilePath = ''

    def isFile(self, fileName):
        if('.' in fileName):
            return True
        return False

    def dirOrFile(self, fileName):
        if(self.isFile(fileName)):
            return "File"
        return "Folder"

    def createNode(self, fileName, treeName):
        fileType = self.dirOrFile(fileName)
        node = treeName.createNode(fileName, fileType)
        return node

    def attachToParent(self, node, tree, array):
        print node.name, node.fileType, tree.root.name
        #count the number of '' in array
        count = 0
        for fileName in array:
            if (fileName == ''):
                count = count+1
        ptr = tree.root
        while(count > 1):
            ptr = ptr.childern[-1]
            count = count - 1
        tree.addChild(ptr, node)
        print "Adding node ", node.name, " as a child of ", ptr.name

    def addSubFolder(self, array):
        print array
        #is a root file/dir
        if not('' in array):
            t = Tree()
            t.root = self.createNode(array[0], t)
            self.trees.append(t)
            print t.root.name, t.root.fileType
            return
        #Create Node
        node = None
        for fileName in array:
            if(fileName != ''):
                node = self.createNode(fileName, self.trees[-1])
        #add the node
        self.attachToParent(node, self.trees[-1], array)
            
    
    def logic(self, path):
        for folder in  path.split("\n"):
            self.addSubFolder(folder.split("\t"))
        #traverse trees to find longest file Path
        for tree in self.trees:
            tree.dfsTraversal()
            if(len(self.longestFilePath) < len(tree.longestFilePath)):
                self.longestFilePath = tree.longestFilePath
                
    def lengthLongestPath(self, path):
        self.logic(path)
        return len(self.longestFilePath)
        """
        :type input: str
        :rtype: int
        """
#Main
obj1 = Solution()
print obj1.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")

obj2 = Solution()
print obj2.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
