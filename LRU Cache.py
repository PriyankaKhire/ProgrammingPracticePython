# LRU Cache
#https://leetcode.com/problems/lru-cache/
class DLLNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class DLLStack(object):
    def __init__(self):
        self.top = None
        self.bottom = None

    def createNode(self, key, value):
        return DLLNode(key, value)

    def removeNodeAddToTop(self, node):
        #if node is top node do nothing
        if( node == self.top):
            return
        #if node is bottom node
        if(node == self.bottom):
            self.deleteFromBottom()
            self.addNodeFromTop(node)
            return
        #if node is in middle
        self.deleteFromMid(node)
        self.addNodeFromTop(node)

    def addNodeFromTop(self, node):
        if(self.top != None):
            node.previous = self.top
            self.top.next = node
        if(self.top == None):
            self.bottom = node
        self.top = node

    def addFromTop(self, key, value):
        node = self.createNode(key, value)
        self.addNodeFromTop(node)

    def deleteFromMid(self, node):
        #if node is the only one
        if(node == self.top and node == self.bottom):
            self.top = None
            self.bottom = None
            return
        #if node is top
        if(node == self.top):
            self.top = self.top.previous
            self.top.next = None
            return
        #if node is bottom
        if(node == self.bottom):
            self.deleteFromBottom()
            return
        #if node is mid
        previousNode = node.previous
        nextNode = node.next
        nextNode.previous = previousNode
        previousNode.next = nextNode

    def deleteFromBottom(self):
        if(self.bottom == None):
            return
        if(self.bottom == self.top):
            self.top = None
            self.bottom = None
            return
        #Assign new bottom
        self.bottom = self.bottom.next
        #remove pointer from the top node of our current bottom node
        self.bottom.previous = None
        
    def display(self):
        ptr = self.top
        while(ptr != None):
            print [ptr.key, ptr.value],
            ptr = ptr.previous
        print ""

        
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.currentCapacity = 0
        self.index = {}
        self.dllQ = DLLStack()
        """
        :type capacity: int
        """
        

    def get(self, key):
        if not(key in self.index):
            return -1
        node = self.index[key]
        self.dllQ.removeNodeAddToTop(node)
        self.dllQ.display()
        print self.index
        return node.value
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if(self.currentCapacity == self.capacity):
            #delete from queue and index
            k = self.dllQ.bottom.key
            del self.index[k]
            self.dllQ.deleteFromBottom()
            self.currentCapacity = self.currentCapacity - 1
        self.dllQ.addFromTop(key, value)
        self.index[key] = self.dllQ.top
        self.currentCapacity = self.currentCapacity + 1
        self.dllQ.display()
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#Main
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print obj.get(2)
#This solution does not work if keys are not unique
