# Populating Next Right Pointers in Each Node II
#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    
    def checkAllNextNodes(self, child, parent):
        ptr = parent.next
        while(ptr != None and child.next == None):
            if(ptr.left != None):
                child.next = ptr.left
            elif(ptr.right != None):
                child.next = ptr.right
            ptr = ptr.next
        if(child.next != None):
            print child.val, "=>", child.next.val
        else:
            print child.val, "=> None"
            
    def secondPass(self, node):
        if node:
            # set the left pointer
            if(node.left != None and node.left.next == None):
                self.checkAllNextNodes(node.left, node)
            # set the right ptr
            if(node.right != None):
                self.checkAllNextNodes(node.right, node)
            # traverse left
            self.secondPass(node.left)
            # traverse right
            self.secondPass(node.right)
    
    def printTree(self, root):
        queue = [root]
        print root.val
        while(queue):
            top = queue.pop(0)
            print 'parent', top.val, 
            if(top.left):
                print top.left.val,
                queue.append(top.left)
            else:
                print "None",
            if(top.right):
                print top.right.val
                queue.append(top.right)
            else:
                print 'None'
    
    def firstPass(self, node):
        if(node):
            # assign left node to right node
            if(node.left != None and node.right != None):
                node.left.next = node.right
            # traverse left
            self.firstPass(node.left)
            # traverse right
            self.firstPass(node.right)
            
    def connect(self, root):
        self.firstPass(root)
        self.secondPass(root)
        self.printTree(root)
        return root
        """
        :type root: Node
        :rtype: Node
        """
        
