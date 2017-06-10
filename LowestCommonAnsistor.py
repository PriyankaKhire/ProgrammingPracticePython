#Lowest Common ansistor
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

flagA = False
flagB = False
flagRoot = False
def foo (curNode, root, a, b):
    global flagA, flagB, flagRoot
    
    if curNode == None:
        return
    #Do post order traversal
    foo(curNode.getLeft(), root, a, b)
    foo(curNode.getRight(), root, a, b)
    print "root is "+str(root.getData())
    print "current node "+str(curNode.getData())
    print "flagA: "+str(flagA)+" flagB: "+str(flagB)+" flagRoot: "+str(flagRoot)
    #if a is found
    if(curNode.getData() == a):
        print "a found"
        flagA = True
    #if b is found
    if (curNode.getData() == b):
        print "b found"
        flagB = True
    #if root is found
    if(curNode.getData() == root.getData()):
        print "root found"
        flagRoot = True
    #if root is lca
    if(flagA == True and flagRoot == True and flagB == False):
        print "root found "+str(root.getData())
        return 
    if(flagB == True and flagRoot ==True and flagA == False):
        print "root found "+str(root.getData())
        return 
    #if lca is in left
    if (flagA == True and flagB == True and flagRoot == False):
        print "going left"
        flagA = False
        flagB = False
        flagRoot = False
        foo(root.getLeft(), root.getLeft(), a, b)
    #if lca is in right
    if (flagRoot == True and flagA == False and flagB == False):
        print "going right"
        flagA = False
        flagB = False
        flagRoot = False
        foo(root.getRight(), root.getRight(), a, b)
    
    
    
    

#Main Program
root = createNode(1)
node1= addLeft(2, root)
node2 = addRight(3, root)
node3 = addLeft(4, node1)
node4 = addRight(5, node1)
node5 = addLeft(6, node2)
node6 = addRight(7, node2)
foo(root, root, 4, 5)
