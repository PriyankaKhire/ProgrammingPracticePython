from multiprocessing import Queue
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
        return node

    #Pops element from tail of the queue
    def pop(self):
        if(self.isEmpty()):
            print "Cannot pop, queue is empty"
            return False
        #Stores the recently popped
        popped = self.tailNode.getData()
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
        #Return the recently popped item
        return popped

    #This function takes the node and puts it in front of the queue
    def updateQ(self, node):
        if(node == self.headNode):
            return
        prev = node.getPrev()
        nxt = node.getNext()
        if(prev != None):
            prev.setNext(nxt)
        if(nxt != None):
            nxt.setPrev(prev)
        node.setPrev(None)
        node.setNext(self.headNode)
        self.headNode = node
        self.display()

    def display(self):
        ptr = Node()
        ptr = self.headNode
        while(ptr != None):
            print ptr.getData()
            print "\n"
            ptr = ptr.getNext()


class LRUCache(object):

    def __init__(self, capacity):
        self.hash_table = {}
        self.q = DLLqueue(capacity)
        
    #Function returns true if LRU cache is full
    def isFull(self):
        if(self.q.isFull()):
            return True
        return False
        
    #Function returns true if LRU cache is empty
    def isEmpty(self):
        if(self.q.isEmpty()):
            return True
        return False

    def get(self, key):
        #Cannot get anything if cache is empty
        if(self.isEmpty()):
            return -1       
        #Get element from cache
        if key in self.hash_table:
            #Update queue
            qNode = self.hash_table[key][1]
            self.q.updateQ(qNode)
            return self.hash_table[key][0]
        return -1
        

    def put(self, key, value):
        if(self.isFull()):
            #Remove least recently used item
            least_recently_used_item = self.q.pop()
            self.hash_table.pop(least_recently_used_item, None)
            print "Removed "+str(least_recently_used_item)        
        #Put element in hash table
        node_address = self.q.push(key)
        self.hash_table[key] = [value, node_address]
        
        
        


#inputs
cache = LRUCache(3)
cache.put(1, "hi")
cache.put(2, "bye")
cache.put(3, "ho")
cache.put(4, "no")
cache.q.display()
print "---"
print cache.get(2)
