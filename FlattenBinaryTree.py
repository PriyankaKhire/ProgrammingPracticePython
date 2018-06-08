#Flatten binary tree
#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree():
    def __init__(self):
        self.root = None

    def preOrder(self, node, parent, stack):
        if node != None:
            print node.data,
            print "parent node "+str(parent.data), 
            print "stack top is that is prev node is "+str(stack[-1].data)
            stack.append(node)
            self.preOrder(node.left, node, stack)
            self.preOrder(node.right, node, stack)

    def makeAllChildernRight(self):
        ptr = self.root
        while ptr.left!= None or ptr.right != None:
            if ptr.left != None:
                self.addRight(ptr.left, ptr)
            ptr = ptr.right
            
    def preOrder_flatten(self, currNode, parent, stack):
        if currNode != None:
            #if stack top is leaf node then we add current node to it
            prevNode = stack[-1]
            print "previous Node "+str(prevNode.data)+" current Node"+currNode.data+" parent "+parent.data+" stack "+str(stack)
            if prevNode and self.isLeaf(prevNode):
                print "previous node "+prevNode.data+" is a leaf"
                #Detach currNode from parent and attach it to prevNode
                if parent.right == currNode:
                    print "Adding current node "+currNode.data+" as left child of previous node "+prevNode.data
                    parent.right  = None
                    self.addRight(currNode, prevNode)
            #Put currNode in stack to trace previous node
            stack.append(currNode)
            self.preOrder_flatten(currNode.left, currNode, stack)
            self.preOrder_flatten(currNode.right, currNode, stack)

    def flatten(self):
        self.preOrder_flatten(self.root, self.root, [self.root])
        self.makeAllChildernRight()
        print "traversing"
        ptr = self.root
        while ptr != None:
            print ptr.data,
            ptr = ptr.right
                

    def createNode(self, data):
        node = Node(data)
        return node

    def addLeft(self, left, node):
        node.left = left
        return

    def isLeaf(self, node):
        if node.left == None and node.right ==None:
            return True
        return False

    def addRight(self, right, parent):
        parent.right = right
        return

    def createTree(self):
        choice = 1
        q = []
        data = raw_input("Enter data for root")
        self.root = self.createNode(data)
        q.append(self.root)
        while choice == 1:
            if q[0] != None and q[0].left != None and q[0].right != None:
                q.pop(0)
            data = raw_input("enter data for child")
            node = self.createNode(data)
            if q[0].left == None:
                self.addLeft(node, q[0])
            else:
                self.addRight(node, q[0])
            q.append(node)
            choice = input("Would you like to continue adding childern ? yes = 1 and no = 2   ")


#Main Program
o = Tree()
o.createTree()
o.preOrder(o.root, o.root, [o.root])
o.flatten()
