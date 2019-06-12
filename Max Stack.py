#Max Stack
#https://leetcode.com/problems/max-stack/
class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.sameNode = None
        
class DoublyLinkedList(object):
    def __init__(self):
        self.top = None

    def createNode(self, data):
        return LinkedListNode(data)

    def addNodeFromTop(self, data):
        node = self.createNode(data)
        if(self.top != None):
            node.prev = self.top
            self.top.next = node
        self.top = node
        return node

    def sortedInsert(self, data, sNode):
        print "inserting ", data
        node = self.createNode(data)
        node.sameNode = sNode
        if(self.top == None):
            self.top = node
            return
        ptr = self.top
        previousPtr = ptr
        while(ptr != None):
            if(ptr.data < data):
                break
            previousPtr = ptr
            ptr = ptr.prev
        #inserting at end
        if(ptr == None):
            previousPtr.prev = node
            node.next = previousPtr
            return
        #inserting in the middle
        if(ptr.next != None):
            ptr.next.prev = node
            node.next = ptr.next
        #inserting at beginning
        ptr.next = node
        node.prev = ptr

    def removeNode(self, node):
        print "removing node", node.data
        if (node == self.top):
            self.removeTopNode()
            return
        if(node.next != None):
            node.next.prev = node.prev
        if(node.prev != None):
            print "previous not none", node.prev.next
            node.prev.next = node.next
            print "previous not none", node.prev.next

    def removeTopNode(self):
        if(self.top.prev != None):
            self.top.prev.next = None
            self.top = self.top.prev
        else:
            self.top = None

    def display(self):
        ptr = self.top
        while(ptr != None):
            print ptr.data,
            ptr = ptr.prev
        print ""
    
class MaxStack(object):

    def __init__(self):
        #Holds all max elements node
        self.mStack = DoublyLinkedList()
        self.stack = DoublyLinkedList()
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        node = self.stack.addNodeFromTop(x)
        #inserted in sorted mStack
        self.mStack.sortedInsert(x, node)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        top = self.stack.top.data
        if(self.stack.top.data == self.mStack.top.data):
            self.mStack.removeTopNode()
        self.stack.removeTopNode()
        return top
        """
        :rtype: int
        """
        

    def top(self):
        return self.stack.top.data
        """
        :rtype: int
        """
        

    def peekMax(self):
        return self.mStack.top.data
        """
        :rtype: int
        """
        

    def popMax(self):
        data = self.mStack.top.data
        node = self.mStack.top
        self.stack.removeNode(node)
        self.mStack.removeTopNode()
        return data
        """
        :rtype: int
        """
        


# Main
obj = MaxStack()
obj.push(5)
obj.stack.display()
obj.mStack.display()
obj.push(1)
obj.stack.display()
obj.mStack.display()
print obj.popMax()
obj.stack.display()
obj.mStack.display()
#print obj.peekMax()
#obj.stack.display()
