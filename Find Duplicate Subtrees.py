# Find Duplicate Subtrees
#Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
#Two trees are duplicate if they have the same structure with same node values.
#
#Example 1:
#
#        1
#       / \
#      2   3
#     /   / \
#    4   2   4
#       /
#      4
#The following are two duplicate subtrees:
#
#      2
#     /
#    4
#and
#
#    4
#Therefore, you need to return above trees' root in the form of a list.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.rlink = None
        self.llink = None
class Tree(object):
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.llink)
            print node.data
            self.inorder(node.rlink)
        
    def createNode(self, data):
        return Node(data)

    def addLeftLink(self, node, link):
        node.llink = link

    def addRightLink(self,node, link):
        node.rlink = link

    def createTree(self, nodeList):
        q = []
        for tnode in nodeList:
            #create root
            if self.root == None:
                self.root = self.createNode(tnode)
                q.append(self.root)
                continue
            #pop the top if both its left and right nodes are filled
            if(q[0].llink != None and q[0].rlink != None):
                q.pop(0)
            top  = q[0]
            node = 0
            if(tnode != "null"):
                node = self.createNode(tnode)
                q.append(node)
            if(top.llink == None):
                self.addLeftLink(top, node)
            else:
                self.addRightLink(top, node)
            
class DuplicateSubTree(object):
    def __init__(self):
        self.hash = {}
        self.duplicateList = []

    #returns true if 2 trees are equal
    def compare2Trees(self, node1, node2):
        q1 = [node1]
        resultQ = []
        q2 = [node2]
        while q1 or q2:
            top1 = q1.pop(0)
            top2 = q2.pop(0)
            if top1:
                resultQ.append(top1.data)
            if (top1 or top2) and ((top1 == None or top2 == None or top1 == 0 or top2 == 0) or (top1.data != top2.data)):
                return False, -1
            if top1.llink or top2.llink :
                q1.append(top1.llink)
                q2.append(top2.llink)
            if top1.rlink or top2.rlink :
                q1.append(top1.rlink)
                q2.append(top2.rlink)
        if q1 or q2:
            return False, -1
        return True, resultQ

    def goThroughNodes(self, nodeList, otherNode):
        duplicate = False
        resultQ = None
        for node in nodeList:
            flag, resultQ = self.compare2Trees(node, otherNode)
            if(flag):
                duplicate = True
                break
        if not duplicate:
            nodeList.append(otherNode)
        else:
            if not resultQ in self.duplicateList:
                self.duplicateList.append(resultQ)
        return nodeList

    
    def findDuplicates(self, root):
        if root:
            if root.data not in self.hash:
                self.hash[root.data] = [root]
            else:
                #we may have a duplicate
                self.hash[root.data] = self.goThroughNodes(self.hash[root.data], root)
            self.findDuplicates(root.llink)
            self.findDuplicates(root.rlink)
        

#Main Program
null = "null"
t = Tree()
t.createTree([1,2,1,3,4,2,1,null, null, null, null, 3,4,2,1,null, null, null, null, 3,4,2,1])

t2 = Tree()
t2.createTree([1,2,2,3,4,3,4,null, null,5,6,null, null, 5, 6])

dst = DuplicateSubTree()
dst.findDuplicates(t.root)
print dst.duplicateList

dst2 = DuplicateSubTree()
dst2.findDuplicates(t2.root)
print dst2.duplicateList
