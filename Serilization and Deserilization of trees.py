#Serialization and Deserialization of different types of trees
class BinaryNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def createNode(self, data):
        node = BinaryNode(data)
        return node

    def addLeft(self, parent, leftNode):
        parent.left = leftNode

    def addRight(self, parent, rightNode):
        parent.right = rightNode

    def createTree(self):
        q = []
        rootVal = raw_input("Add value to root ")
        self.root = self.createNode(rootVal)
        q.append(self.root)
        ch = "y"
        while(ch == "y"):
            val = raw_input("\n Enter node value")
            node = self.createNode(val)
            if(q[0].left != None and q[0].right != None):
                q.pop(0)
            if(q[0].left == None):
                self.addLeft(q[0], node)
            else:
                self.addRight(q[0], node)
            q.append(node)
            ch = raw_input("\n continue ? y/n")
        #print tree
        print "Printing inorder traversal of tree"
        self.display(self.root)

    def display(self, root):
        if root:
            self.display(root.left)
            print root.data
            self.display(root.right)

class SerilizationBinary(object):
    def __init__(self, root):
        self.root = root
        self.inorderString = ""
        self.preorderString = ""

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorderString = self.inorderString + " " + root.data
            self.inorder(root.right)
            
    def preorder(self, root):
        if root:
            self.preorderString = self.preorderString +" "+root.data
            self.preorder(root.left)
            self.preorder(root.right)

    def serilize(self):
        self.inorder(self.root)
        self.preorder(self.root)
        print self.inorderString
        print self.preorderString

class DeserilizationBinary(BinaryTree):
    def __init__(self, inorder, preorder):
        self.inorder = inorder.strip().split(" ")
        self.preorder = preorder.strip().split(" ")
        self.inorderPosHash = {}
        self.root = None

    def insertInInorderPosHash(self):
        for i in range(len(self.inorder)):
            self.inorderPosHash[self.inorder[i]] = i

    #what side is the child on the parent in inorder string
    def whatSide(self, parent, child):
        if(self.inorderPosHash[parent] < self.inorderPosHash[child]):
            return "Right"
        return "Left"

    def addToRightOrLeft(self, stack, currentNode):
        side = "Right"
        popped = None
        while ( (stack) and (side == "Right")):
            popped = stack.pop()
            if stack:
                side = self.whatSide(stack[-1].data, currentNode.data)
        #Add to right
        side = self.whatSide(popped.data, currentNode.data)
        if(side == "Left"):
            self.addLeft(popped, currentNode)
        else:
            self.addRight(popped, currentNode)


    def solution(self):
        self.insertInInorderPosHash()
        stack = []
        #start reading preorder string
        for element in self.preorder:
            #create node
            node = self.createNode(element)
            #if we don't have root
            if self.root == None:
                self.root = node
            else:
                #find side of node in inorder travarsal of stack top
                side = self.whatSide(stack[-1].data, element)
                if(side == "Left"):
                    self.addLeft(stack[-1], node)
                else:
                    self.addToRightOrLeft(stack, node)
            stack.append(node)
        print "printing inorder of newly created tree"
        self.display(self.root)
            
        

class NaryNode(object):
    def __init__(self, val):
        self.data = val
        self.links = []

class NaryTree(object):
    def __init__(self):
        self.root = None

    def createNode(self,val):
        node = NaryNode(val)
        return node

    def addLink(self, parent, child):
        parent.links.append(child)

    def createTree(self):
        q = []
        rootVal = raw_input("Add value to root ")
        self.root = self.createNode(rootVal)
        q.append(self.root)
        ch = "y"
        while(ch == "y"):
            addTo_parent = raw_input("\n Current Parent is "+str(q[0].data)+"\n do you wanna add to current parent? y/n")
            if (addTo_parent == "n"):
                q.pop(0)
            val = raw_input("\n enter value for the node ")
            node = self.createNode(val)
            self.addLink(q[0], node)
            q.append(node)
            ch = raw_input("\n continue ? y/n")
        print "displaying Nary tree in level order"
        self.display()

    def display(self):
        if self.root:
            q = []
            q.append(self.root)
            while q:
                top = q.pop(0)
                print top.data
                for node in top.links:
                    q.append(node)
            

class SerilizationNary(object):
    def __init__(self, root):
        self.root = root
        self.output = ""

    def logic(self, root):
        if root:
            self.output = self.output+" "+root.data
            for child in root.links:
                self.logic(child)
            self.output = self.output+" )"
                

    def dfs(self):
        self.logic(self.root)
        print self.output

class DeserilizationNary(NaryTree):
    def __init__(self, string):
        self.input = string.strip().split(" ")
        print self.input

    def iterativeDFS(self):
        stack = []
        self.root = self.createNode(self.input[0])
        stack.append(self.root)
        self.input.pop(0)
        for data in self.input:
            if data == ")":
                stack.pop()
            else:
                node = self.createNode(data)
                self.addLink(stack[-1], node)
                stack.append(node)
        self.display()
          
        


#Main Program

b = BinaryTree()
b.createTree()

sb = SerilizationBinary(b.root)
sb.serilize()

dsb = DeserilizationBinary(sb.inorderString, sb.preorderString)
dsb.solution()

n= NaryTree()
n.createTree()

s = SerilizationNary(n.root)
s.dfs()

d = DeserilizationNary(s.output)
d.iterativeDFS()      
