#Flip Binary Tree
#https://www.geeksforgeeks.org/flip-binary-tree/
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def createNode(self, data):
        return TreeNode(data)

    def addNode(self, parent, data, side):
        node = self.createNode(data)
        if(side == 'left'):
            parent.left = node
        else:
            parent.right = node
        return node

    def createCompleteTree(self, array):
        q = []
        for data in array:
            if(self.root == None):
                self.root = self.createNode(data)
                q.append(self.root)
            else:
                # if q top has both left and right child then pop it from queue
                if(q[0].left != None and q[0].right != None):
                    q.pop(0)
                top = q[0]
                node = None
                if(top.left == None):
                    node = self.addNode(top, data, 'left')
                else:
                    node = self.addNode(top, data, 'right')
                # Add current node
                q.append(node)

    def inorder(self, node):
        if not(node):
            return
        self.inorder(node.left)
        print node.data,
        self.inorder(node.right)

    def levelorder(self, node):
        q = [node]
        while q:
            top = q.pop(0)
            print top.data,
            if(top.left != None):
                q.append(top.left)
            if(top.right != None):
                q.append(top.right)

    def display(self):
        print "inorder"
        self.inorder(self.root)
        print "\nlevel order"
        self.levelorder(self.root)
        print "\n"

class FlipTree(object):
    def __init__(self):
        self.tree = Tree()
        self.tree.createCompleteTree([1,2,3,4,5,6,7])
        self.tree.display()
        self.sibblingAndParentHash = {}

    def findLeftMostNodes(self, node, nodes):
        if not node:
            return
        self.findLeftMostNodes(node.left, nodes)
        nodes.append(node)

    def logic(self):
        # traverse tree and find all left most nodes 
        leftNodes = []
        self.findLeftMostNodes(self.tree.root, leftNodes)
        # Put all parents and sibblings in the hash.
        parent = None
        for leftNode in reversed(leftNodes):
            if(parent == None):
                self.sibblingAndParentHash[leftNode] = [None, None]
            else:
                self.sibblingAndParentHash[leftNode] = [parent, parent.right]
            parent = leftNode
        # disallocate all the left node's left and right childern
        for leftNode in leftNodes:
            leftNode.left = None
            leftNode.right = None
        # go through the left nodes and attach parent as right node and sibling as left node
        for leftNode in leftNodes:
            if(self.sibblingAndParentHash[leftNode][0] != None and self.sibblingAndParentHash[leftNode][1] != None):
                leftNode.left = self.sibblingAndParentHash[leftNode][1]
                leftNode.right = self.sibblingAndParentHash[leftNode][0]
        self.tree.root = leftNodes[0]
        # display.
        self.tree.display()
    
#Main
obj = FlipTree()
obj.logic()
