#Binary Tree

class node():
    def __init__(self):
        self.data = None
        self.lLink = None
        self.rLink = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setRLink(self, link):
        self.rLink = link
    def getRLink(self):
        return self.rLink
    def setLLink(self, link):
        self.lLink = link
    def getLLink(self):
        return self.lLink

class Tree():
    def createNode(self, data):
        newNode = node()
        newNode.setData(data)
        return newNode
    def addLeftNode(self, root, data):
        n = self.createNode(data)
        root.setLLink(n)
    def addRightNode(self, root, data):
        n = self.createNode(data)
        root.setRLink(n)
    def createTree(self):
        data = raw_input("Enter data for root node: ")
        root = self.createNode(int(data))
        ch = True
        print "Adding More nodes"
        while(ch):
            data = int(raw_input("Enter data : "))
            #Find a place to insert node
            ptr = root
            prev = ptr
            while(ptr != None):
                prev = ptr
                if(ptr.getData() > data):
                    #Go left
                    ptr = ptr.getLLink()
                else:
                    #Go Right
                    ptr = ptr.getRLink()
            #Now that we have the node
            if(prev.getData() > data):       
                self.addLeftNode(prev, data)
            else:
                self.addRightNode(prev, data)
            ch = raw_input("Wanna continue y/n \n")
            if(ch == "y"):
                ch = True
            else:
                ch = False
        return root
    
    def inorder(self, root):
        if(root != None):
            self.inorder(root.getLLink())
            print root.getData() ,
            self.inorder(root.getRLink())
    def postorder(self, root):
        if(root != None):
            self.postorder(root.getLLink())
            self.postorder(root.getRLink())
            print root.getData() ,
    def preorder(self, root):
        if(root != None):
            print root.getData() ,
            self.preorder(root.getLLink())
            self.preorder(root.getRLink())
    def height(self, root):
        if root == None:
            return 0
        else:
            l = self.height(root.getLLink())
            r = self.height(root.getRLink())
            if l > r:
                return l+1
            return r+1
            

#Main Program
t = Tree()
r = t.createTree()
print "\ninorder"
t.inorder(r)
print "\n post order"
t.postorder(r)
print "\n pre order"
t.preorder(r)
print "\n height"
print t.height(r)
