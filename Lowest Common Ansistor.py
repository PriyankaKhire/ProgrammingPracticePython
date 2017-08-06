#Lowest common ansistor of 2 nodes
n1Flag = False
n2Flag = False
rFlag = False

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
    
    def findNodes(self, root, n1, n2, r):
        global n1Flag, n2Flag, rFlag
        #In order traversal
        if root != None:
            self.findNodes(root.getLLink(), n1, n2, r)
            print root.getData()
            #If nodes are found 
            if (root.getData() == n1):
                print "Found n1"
                n1Flag = True
            if( root.getData() == n2):
                print "Found n2"
                n2Flag = True
            if(root.getData() == r):
                print "Found r"
                rFlag = True
            #Now check which all nodes are found
            #Nodes are on left
            print "Flags n1 = "+str(n1Flag)+" n2 = "+str(n2Flag)+" r = "+str(rFlag)
            print "Left ? "+str(n1Flag  and n2Flag and (not rFlag)) 
            if(n1Flag  and n2Flag and (not rFlag)):
                return "Left"
            #Nodes are on right
            print "Right ? "+str(rFlag and not n1Flag and not n2Flag)
            if(rFlag and not n1Flag and not n2Flag):
                return "Right"
            #If root is the LCA
            print "Mid ? "+str(n1Flag and rFlag and not n2Flag)
            if(n1Flag and rFlag and not n2Flag):
                return "Mid"
            print "Mid ? "+str(n2Flag and rFlag and not n1Flag)
            if(n2Flag and rFlag and not n1Flag):
                return "Mid"
            self.findNodes(root.getRLink(), n1, n2, r)
                
    #This algo assumes that the 2 nodes are present in tree
    #We can also add additional check to ensure that
    def lca(self, root, data1, data2):
        print self.findNodes(root, data1, data2, root.getData())
        


#Main Program
t = Tree()
r = t.createTree()
t.lca(r, 2, 8)
