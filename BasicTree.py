#Tree data structure and traversals

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

def inorder(root):
    if root == None:
        return
    #Go left
    inorder(root.getLeft())
    print root.getData()
    #Go right
    inorder(root.getRight())

def postorder(root):
    if root == None:
        return
    #Left
    postorder(root.getLeft())
    #Right
    postorder(root.getRight())
    print root.getData()

def preorder(root):
    if root == None:
        return
    print root.getData()
    #Left
    preorder(root.getLeft())
    #Right
    preorder(root.getRight())

q = []
def levelorder(root):
    global q
    if root == None:
        return
    if(root.getLeft() != None):
        q.append(root.getLeft().getData())
    if (root.getRight() != None):
        q.append(root.getRight().getData())
    levelorder(root.getLeft())
    levelorder(root.getRight())

#Main Program
root = createNode(1)
node1= addLeft(2, root)
node2 = addRight(3, root)
node3 = addLeft(4, node1)
node4 = addRight(5, node1)
node5 = addLeft(6, node2)
node6 = addRight(7, node2)
inorder(root)
print "\n\n"
postorder(root)
print "\n\n"
preorder(root)
q.append(root.getData())
levelorder(root)
print q
