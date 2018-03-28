#Doubly Linked List queue
from multiprocessing import Queue
class Node(object):
    def __init__(self):
        self.data = None
        self.prevPtr = None
        self.nextPtr = None

    def setData(self, data):
        self.data = data

    def setPrev(self, prevPtr):
        self.prevPtr = prevPtr

    def setNext(self, nextPtr):
        self.nextPtr = nextPtr

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prevPtr

    def getNext(self):
        return self.nextPtr

#Has functions pop, push, is empty and is full
class DLLqueue(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.headNode = None
        self.tailNode = None
        self.elementCount = 0

    def createNode(self, data):
        newNode = Node()
        newNode.setData(data)
        return newNode

    def isEmpty(self):
        if (self.elementCount == 0):
            return True
        return False

    def isFull(self):
        if (self.elementCount == self.capacity):
            return True
        return False

    #add elements from the front of queue 
    def push(self, data):
        #if queue is not full
        if(self.isFull()):
            print "Cannot push in queue, its full"
            return False
        #Create new node for queue
        node = self.createNode(data)
        #Check if its the first node to be added
        if(self.headNode == None and self.tailNode == None):
            self.headNode = node
            self.tailNode = node
        else:
            #Add node from front
            node.setNext(self.headNode)
            self.headNode.setPrev(node)
            #Update head node
            self.headNode = node
        #update the element count
        self.elementCount = self.elementCount + 1

    #Pops element from tail of the queue
    def pop(self):
        if(self.isEmpty()):
            print "Cannot pop, queue is empty"
            return False
        #Check if it's the last node
        if(self.headNode == self.tailNode):
            self.headNode = None
            self.tailNode = None
        else:
            #Pop the node from tail
            prev = self.tailNode.getPrev()
            prev.setNext(None)
            self.tailNode.setPrev(None)
            #Update prev node.
            self.tailNode = prev
        #Update element count
        self.elementCount = self.elementCount - 1
            
        
    def display(self):
        ptr = Node()
        ptr = self.headNode
        while(ptr != None):
            print ptr.getData()
            print "\n"
            ptr = ptr.getNext()

#Main Program
q = DLLqueue(3)
q.push(1)
q.push(2)
q.push(3)
q.display()
q.push(4)
print 'pop'
q.pop()
q.pop()
q.pop()
q.display()
q.pop()
