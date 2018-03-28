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
        #if head is null then assign it
        if(not self.headNode):
            self.headNode = newNode
        if(not self.tailNode):
            self.tailNode = newNode
        print newNode
        print newNode.getNext
        print newNode.getPrev
        return newNode

    def isEmpty(self):
        if (self.headNode == None):
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
        #Add it from head of the queue
        node.setNext(self.headNode)
        self.headNode.setPrev(node)
        #update head of the queue
        self.headNode = node
        #update the element count
        self.elementCount = self.elementCount + 1
        

#######################
        #Error in display and push function of queue, to check
        #########################
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
        self.q = Queue(maxsize=capacity)
        print self.q
        
    #Function returns true if LRU cache is full
    def isFull(self):
        if(self.q.full()):
            return True
        return False
        
    #Function returns true if LRU cache is empty
    def isEmpty(self):
        if(self.q.empty()):
            return True
        return False

    def get(self, key):
        #Cannot get anything if cache is empty
        if(self.isEmpty()):
            return -1
        
        #Get element from cache
        if key in self.hash_table:
            return self.hash_table[key]
        return -1
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if(self.isFull()):
            #Remove least recently used item
            least_recently_used_item = self.q.get
            self.hash_table.pop(least_recently_used_item, None)
            print "Removed "+str(least_recently_used_item)
        
        #Put element in hash table
        self.hash_table[key] = value
        self.q.put(key)
        
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        


#inputs
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print cache.get(1);  
q = DLLqueue(4)
q.push(1)
q.push(2)

