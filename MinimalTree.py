#Minimal Tree
#Given a sorted array, create BST from it

class node():
    def __init__(self):
        self.data  = None
        self.rlink = None
        self.llink = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setRlink(self,link):
        self.rlink = link
    def setLlink(self, link):
        self.llink = link
    def getRlink(self):
        return self.rlink
    def getLlink(self):
        return self.llink
class bst():
    def createNode(self, data):
        n = node()
        n.setData(data)
        return n
    def addLeft(self, data, root):
        n = self.createNode(data)
        root.setLlink(n)
        return n
    def addRight(self, data, root):
        n = self.createNode(data)
        root.setRlink(n)
        return n
    def getMid(self, a):
        if a:
            m = len(a)/2
            return m
        return False
    def addNode(self, root, data):
        ptr = root
        prev = ptr
        while(ptr != None):
            prev = ptr
            if(ptr.getData() < data):
                #Go right
                ptr = ptr.getRlink()
            else:
                #Go left
                ptr = ptr.getLlink()
        #Add node
        if (prev.getData() < data):
            #Add right
            print "Adding node "+str(data)+" to parent "+str(prev.getData())+" on the right"
            n = self.addRight(data, prev)
        else:
            #Add left
            print "Adding node "+str(data)+" to parent "+str(prev.getData())+" on the left"
            n = self.addLeft(data, prev)
        return n
    
    def createBST(self, a, root):
        if a:
            #Get mid element
            m = self.getMid(a)
            if(len(a) == 1):
                n = self.addNode(root, a[0])
            print "Mid is "+str(a[m])
            #If there is no mid element then return
            if not m:
                print "Returning"
                return
            #Add node to root
            if(root == None):
                print "Root of the tree is "+str(a[m])
                root = self.createNode(a[m])
                mid_node = root
            else:
                print "Trying to find place to add node "+str(a[m])
                #Find place to add the node
                mid_node = self.addNode(root, a[m])
            #Recurse
            print "making tree for "+str(a[:m])
            self.createBST(a[:m], mid_node)
            print "Making tree for "+str(a[m+1:])
            self.createBST(a[m+1:], mid_node)

#Main Program
t = bst()
t.createBST([1,2,3,4,5,6,7], None)
            
                
            
        
