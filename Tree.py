#Tree
class node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def setData(self, data):
        self.data = data

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

class LinkedList:
    def createNode(data):
        newNode = node()
        newNode.setData(data)
        return newNode

    def addLeft(data, root):
        lnode = createNode(data)
        root.setLeft(lnode)
        return lnode

    def addRight(data, root):
        rnode = createNode(data)
        root.setRight(rnode)
        return rnode
    
